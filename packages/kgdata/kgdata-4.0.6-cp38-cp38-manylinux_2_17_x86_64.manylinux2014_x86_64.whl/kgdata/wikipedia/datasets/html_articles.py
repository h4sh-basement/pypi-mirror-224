import tarfile
from datetime import datetime
from functools import partial
from typing import BinaryIO, Iterable, Union, cast

import orjson

from kgdata.dataset import Dataset
from kgdata.db import deser_from_dict
from kgdata.spark import are_records_unique, does_result_dir_exist
from kgdata.splitter import split_a_file
from kgdata.wikipedia.config import WikipediaDirCfg
from kgdata.wikipedia.models.html_article import HTMLArticle


def html_articles() -> Dataset[HTMLArticle]:
    """
    Extract HTML page

    Returns:
        Dataset[HTMLArticle]
    """
    cfg = WikipediaDirCfg.get_instance()

    dump_file = cfg.get_html_article_file()
    need_double_check = False

    if not does_result_dir_exist(cfg.html_articles / "splitted"):
        with tarfile.open(dump_file, "r:*") as archive:
            for file in archive:
                split_a_file(
                    infile=lambda: (
                        file.size,
                        cast(BinaryIO, archive.extractfile(file)),
                    ),
                    outfile=cfg.html_articles
                    / "splitted"
                    / file.name.split(".", 1)[0]
                    / "part.ndjson.gz",
                    n_writers=8,
                    override=True,
                    n_records_per_file=3000,
                )
        (cfg.html_articles / "_SUCCESS").touch()

    if not does_result_dir_exist(cfg.html_articles / "final"):
        # sometimes, we may have multiple html of the same URL (for different revisions), we choose to keep the
        # latest one only.
        (
            Dataset(
                cfg.html_articles / "splitted/*/*.gz",
                deserialize=lambda line: HTMLArticle.from_dump_dict(orjson.loads(line)),
            )
            .get_rdd()
            .map(
                lambda a: (a.url, a)
            )  # same url but may have different page id such as draft.
            .reduceByKey(select_updated_article)
            .map(lambda tup: (tup[1].page_id, tup[1]))
            .reduceByKey(select_updated_article)
            .map(lambda tup: tup[1])
            .map(ser_html_articles)
            .coalesce(1024, shuffle=True)
            .saveAsTextFile(
                str(cfg.html_articles / "final"),
                compressionCodecClass="org.apache.hadoop.io.compress.GzipCodec",
            )
        )

        need_double_check = True

    ds = Dataset(
        cfg.html_articles / "final/*.gz",
        deserialize=partial(deser_from_dict, HTMLArticle),
    )
    if need_double_check:
        assert are_records_unique(ds.get_rdd(), lambda a: a.url)
        assert are_records_unique(ds.get_rdd(), lambda a: a.page_id)
        assert are_records_unique(ds.get_rdd(), lambda a: a.name)
    return ds


def deser_html_articles(line: Union[str, bytes]) -> HTMLArticle:
    return HTMLArticle.from_dict(orjson.loads(line))


def ser_html_articles(article: HTMLArticle) -> bytes:
    return orjson.dumps(article.to_dict())


def find_latest_articles(articles: Iterable[HTMLArticle]) -> HTMLArticle:
    return max(articles, key=lambda a: datetime.fromisoformat(a.date_modified))


def select_updated_article(article1: HTMLArticle, article2: HTMLArticle) -> HTMLArticle:
    dt1 = datetime.fromisoformat(article1.date_modified)
    dt2 = datetime.fromisoformat(article2.date_modified)

    if dt1 > dt2:
        return article1
    else:
        return article2
