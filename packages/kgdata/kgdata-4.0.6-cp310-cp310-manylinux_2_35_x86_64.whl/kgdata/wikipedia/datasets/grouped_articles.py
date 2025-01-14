import gzip
from typing import List, Tuple, TypedDict

import orjson
from kgdata.dataset import Dataset
from kgdata.spark import does_result_dir_exist
from kgdata.wikipedia.config import WikipediaDirCfg
from kgdata.wikipedia.datasets.articles import articles
from serde.helper import get_open_fn
from tqdm import tqdm


class GroupedArticles(TypedDict):
    # (title, id)
    final: Tuple[str, str]
    group: List[Tuple[str, str]]


def grouped_articles() -> Dataset[GroupedArticles]:
    """Group wikipedia pages/articles that are belong to the same entity"""
    cfg = WikipediaDirCfg.get_instance()
    batch_size = 64000

    if not does_result_dir_exist(cfg.grouped_articles):
        wiki_links = []
        for infile in tqdm(articles().get_files(), desc="read file"):
            with get_open_fn(infile)(infile, "rb") as f:
                for line in f:
                    r = orjson.loads(line)
                    wiki_links.append((r["id"], r["title"], r["redirect_title"]))

        # verify if we have the case of one source node is link to two target nodes, then we build dict that manually curate those nodes
        tmp = {}
        manually_curated_source2target = {}
        title2id = {}
        for source_id, source, target in tqdm(wiki_links):
            if source not in tmp:
                tmp[source] = target
                title2id[source] = source_id
            else:
                assert source not in manually_curated_source2target
                if target is None:
                    manually_curated_source2target[source] = tmp[source]
                    # don't have to update the id since this we discard this article
                else:
                    manually_curated_source2target[source] = target
                    title2id[source] = source_id

                print("`%s` | `%s` | `%s`" % (source, target, tmp[source]))

        # build reverse map
        reverse_map = {}
        leaves = set()
        for source_id, source, target in tqdm(wiki_links, desc="build reverse map"):
            if source in manually_curated_source2target:
                continue

            if target is None:
                assert source not in leaves
                leaves.add(source)
                continue

            if target not in reverse_map:
                reverse_map[target] = [source]
            else:
                reverse_map[target].append(source)

        for source, target in manually_curated_source2target.items():
            if target is None:
                leaves.add(source)
                continue
            if target not in reverse_map:
                reverse_map[target] = [source]
            else:
                reverse_map[target].append(source)

        # now travel upward to group
        visited = set()

        def trace_upward(reverse_map, group, ptr):
            assert ptr not in visited
            visited.add(ptr)

            for parent in reverse_map.get(ptr, []):
                group.append((parent, title2id[parent]))
                trace_upward(reverse_map, group, parent)

        groups: List[GroupedArticles] = []
        for leaf in tqdm(leaves, desc="grouping"):
            if leaf not in reverse_map:
                groups.append(
                    {"final": (leaf, title2id[leaf]), "group": [(leaf, title2id[leaf])]}
                )
            else:
                group = [(leaf, title2id[leaf])]
                trace_upward(reverse_map, group, leaf)
                groups.append({"group": group, "final": (leaf, title2id[leaf])})

        # write result
        count = 0
        cfg.grouped_articles.mkdir(parents=True, exist_ok=True)

        for i in tqdm(range(0, len(groups), batch_size), desc="writing result"):
            with gzip.open(
                cfg.grouped_articles / ("part.%05d.ndjson.gz" % count), "wb"
            ) as f:
                for g in groups[i : i + batch_size]:
                    f.write(orjson.dumps(g))
                    f.write(b"\n")
                count += 1

        (cfg.grouped_articles / "_SUCCESS").touch()

    return Dataset(cfg.grouped_articles / "*.gz", deserialize=orjson.loads)
