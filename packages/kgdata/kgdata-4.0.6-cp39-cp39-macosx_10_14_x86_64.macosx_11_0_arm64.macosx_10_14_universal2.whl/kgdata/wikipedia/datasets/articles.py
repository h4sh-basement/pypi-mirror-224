import xml.etree.ElementTree as ET
from bz2 import BZ2File
from gzip import GzipFile
from typing import BinaryIO, Union

import orjson
from kgdata.dataset import Dataset
from kgdata.spark import does_result_dir_exist
from kgdata.splitter import split_a_file
from kgdata.wikipedia.config import WikipediaDirCfg
from kgdata.wikipedia.models.page_article import WikiPageArticle


def articles() -> Dataset[WikiPageArticle]:
    """Extract articles from XML dumps"""
    cfg = WikipediaDirCfg.get_instance()

    if not does_result_dir_exist(cfg.articles):
        split_a_file(
            infile=cfg.get_article_file(),
            outfile=cfg.articles / "part.ndjson.gz",
            n_writers=8,
            override=True,
            n_records_per_file=64000,
            record_iter=iter_from_dump,
        )
        (cfg.articles / "_SUCCESS").touch()
    return Dataset(cfg.articles / "*.gz", deserialize=deser_page_article)


def deser_page_article(line: Union[str, bytes]) -> WikiPageArticle:
    return WikiPageArticle.from_dict(orjson.loads(line))


def iter_from_dump(infile: Union[BZ2File, GzipFile, BinaryIO]):
    # this seems to be the only way to specify default namespace in python 3.7
    ET.register_namespace("", "http://www.mediawiki.org/xml/export-0.10/")

    tree = iter(
        ET.iterparse(
            infile,
            events=(
                "start",
                "end",
            ),
        )
    )
    event, root = next(tree)

    for event, elem in tree:
        if (
            event != "end"
            or elem.tag != "{http://www.mediawiki.org/xml/export-0.10/}page"
        ):
            continue

        id = elem.find("{http://www.mediawiki.org/xml/export-0.10/}id").text
        ns = elem.find("{http://www.mediawiki.org/xml/export-0.10/}ns").text
        title = elem.find("{http://www.mediawiki.org/xml/export-0.10/}title").text
        redirect_title = elem.find(
            "{http://www.mediawiki.org/xml/export-0.10/}redirect"
        )
        if redirect_title is not None:
            redirect_title = redirect_title.get("title")
        model = elem.find(
            "{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}model"
        ).text
        format = elem.find(
            "{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}format"
        ).text
        text = (
            elem.find(
                "{http://www.mediawiki.org/xml/export-0.10/}revision/{http://www.mediawiki.org/xml/export-0.10/}text"
            ).text
            or ""
        )

        yield orjson.dumps(
            WikiPageArticle(
                id, ns, title, redirect_title, model, format, text
            ).to_dict()
        )

        # avoid using too much memory, remove the elem. leverage the fact that pages_articles if mediawiki > page
        root.remove(elem)
