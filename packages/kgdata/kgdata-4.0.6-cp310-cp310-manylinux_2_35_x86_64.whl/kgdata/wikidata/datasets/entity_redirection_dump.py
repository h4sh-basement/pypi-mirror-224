from bz2 import BZ2File
from gzip import GzipFile
from typing import BinaryIO, Union

from kgdata.dataset import Dataset
from kgdata.splitter import split_a_file
from kgdata.wikidata.config import WikidataDirCfg


def entity_redirection_dump() -> Dataset[str]:
    """Wikidata entity redirections"""
    cfg = WikidataDirCfg.get_instance()

    split_a_file(
        infile=cfg.get_redirect_dump_file(),
        outfile=cfg.entity_redirection_dump / "part.sql.gz",
        record_iter=_record_iter,
        record_postprocess="kgdata.wikidata.datasets.entity_redirection_dump._record_postprocess",
        n_writers=8,
        override=False,
    )

    return Dataset.string(cfg.entity_redirection_dump / "*.gz")


def _record_iter(f: Union[BZ2File, GzipFile, BinaryIO]):
    for line in f:
        if line.startswith(b"INSERT INTO"):
            yield line
            break
    for line in f:
        yield line


def _record_postprocess(line: bytes):
    if not line.startswith(b"INSERT INTO"):
        assert line.startswith(b"/*") or line == b"\n" or line.startswith(b"--"), line
        return None
    return line.rstrip(b"\r\n")


if __name__ == "__main__":
    WikidataDirCfg.init("/data/binhvu/sm-dev/data/wikidata/20211213")
    entity_redirection_dump()
