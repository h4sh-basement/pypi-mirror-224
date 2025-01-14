from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Literal, Optional

from kgdata.models.multilingual import MultiLingualString, MultiLingualStringList
from kgdata.wikidata.models.wdstatement import WDStatement
from kgdata.wikidata.models.wdvalue import WDValue


@dataclass
class WDEntity:
    __slots__ = (
        "id",
        "type",
        "datatype",
        "label",
        "description",
        "aliases",
        "props",
        "sitelinks",
    )

    id: str
    # possible values ["item", "property"]
    type: Literal["item", "property"]
    label: MultiLingualString
    # the datatype is not described in the documentation: https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON
    # however, seems to appear for the property, and will tell us whether the property is an external identifier or not
    # possible values:
    # ['quantity', 'wikibase-form', 'geo-shape', 'math', 'wikibase-item', 'musical-notation', 'commonsMedia', 'wikibase-property', 'wikibase-lexeme', 'tabular-data', 'time', 'wikibase-sense', 'external-id', 'monolingualtext', 'string', 'globe-coordinate', 'url']
    datatype: Optional[str]
    description: MultiLingualString
    aliases: MultiLingualStringList
    props: Dict[str, List[WDStatement]]
    sitelinks: Dict[str, SiteLink]

    def instance_of(self) -> list[str]:
        instanceof = []
        for stmt in self.props.get("P31", []):
            if WDValue.is_entity_id(stmt.value):
                instanceof.append(stmt.value.as_entity_id())
        return instanceof

    def get_object_prop_value(self, prop: str) -> list[str]:
        lst = []
        for stmt in self.props.get(prop, []):
            if WDValue.is_entity_id(stmt.value):
                lst.append(stmt.value.as_entity_id())
        return lst

    def shallow_clone(self):
        return WDEntity(
            id=self.id,
            type=self.type,
            label=self.label,
            datatype=self.datatype,
            description=self.description,
            aliases=self.aliases,
            props=self.props,
            sitelinks=self.sitelinks,
        )

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "label": self.label.to_dict(),
            "datatype": self.datatype,
            "description": self.description.to_dict(),
            "aliases": self.aliases.to_dict(),
            "props": {k: [v.to_dict() for v in vals] for k, vals in self.props.items()},
            "sitelinks": {k: v.to_dict() for k, v in self.sitelinks.items()},
        }

    @staticmethod
    def from_dict(o):
        o["props"] = {
            k: [WDStatement.from_dict(v) for v in vals]
            for k, vals in o["props"].items()
        }
        o["sitelinks"] = {k: SiteLink(**v) for k, v in o["sitelinks"].items()}
        o["label"] = MultiLingualString(**o["label"])
        o["description"] = MultiLingualString(**o["description"])
        o["aliases"] = MultiLingualStringList(**o["aliases"])
        return WDEntity(**o)

    def to_tuple(self):
        return (
            self.id,
            self.type,
            self.label.to_tuple(),
            self.datatype,
            self.description.to_tuple(),
            self.aliases.to_tuple(),
            {k: [v.to_tuple() for v in stmts] for k, stmts in self.props.items()},
            {k: v.to_tuple() for k, v in self.sitelinks.items()},
        )

    @staticmethod
    def from_tuple(t):
        t[2] = MultiLingualString(t[2][0], t[2][1])
        t[4] = MultiLingualString(t[4][0], t[4][1])
        t[5] = MultiLingualStringList(t[5][0], t[5][1])
        for stmts in t[6].values():
            for i, stmt in enumerate(stmts):
                stmts[i] = WDStatement.from_tuple(stmt)
        for k, v in t[7].items():
            t[7][k] = SiteLink(v[0], v[1], v[2], v[3])
        return WDEntity(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7])

    @staticmethod
    def from_wikidump(entity: dict, lang: str = "en") -> WDEntity:
        """Extract essential information from qnode in the form that are easier to work with

        Read more about ranks and truthy statements:
            - https://www.wikidata.org/wiki/Help:Ranking
            - https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format#Truthy_statements

        Parameters
        ----------
        qnode : dict
            qnode
        lang : str, optional
            language, default is 'en'

        Returns
        -------
        QNode
        """
        props = {}
        sitelinks = {}

        for prop, stmts in entity["claims"].items():
            prop_value = []
            for stmt in stmts:
                if stmt["rank"] == "deprecated":
                    continue
                mainsnak = stmt["mainsnak"]
                if mainsnak["snaktype"] != "value":
                    assert "datavalue" not in mainsnak
                    continue
                datavalue = mainsnak["datavalue"]

                try:
                    value = datavalue["value"]
                    type = datavalue["type"]
                except:
                    print(datavalue)
                    raise

                qualifiers = {}
                if "qualifiers" in stmt:
                    assert "qualifiers-order" in stmt
                    for qualifier_id, qualifier_snaks in stmt["qualifiers"].items():
                        qualifier_values = []
                        for qualifier_snak in qualifier_snaks:
                            if qualifier_snak["snaktype"] != "value":
                                assert "datavalue" not in qualifier_snak["snaktype"]
                                continue

                            qualifier_dvalue = qualifier_snak["datavalue"]["value"]
                            qualifier_dtype = qualifier_snak["datavalue"]["type"]

                            qualifier_values.append(
                                WDValue(value=qualifier_dvalue, type=qualifier_dtype)
                            )
                        qualifiers[qualifier_id] = qualifier_values
                    qualifiers_order = stmt["qualifiers-order"]
                else:
                    qualifiers_order = []

                prop_value.append(
                    WDStatement(
                        value=WDValue(value=value, type=type),
                        qualifiers=qualifiers,
                        qualifiers_order=qualifiers_order,
                        rank=stmt["rank"],
                    )
                )
            props[prop] = prop_value

        for key, sitelink in entity.get("sitelinks", {}).items():
            sitelinks[key] = SiteLink(
                sitelink["site"],
                sitelink["title"],
                badges=sitelink["badges"],
                url=sitelink.get("url", None),
            )

        label = {k: v["value"] for k, v in entity["labels"].items()}
        if lang not in label:
            label[lang] = ""
        label = MultiLingualString(label, lang)

        description = {k: v["value"] for k, v in entity["descriptions"].items()}
        if lang not in description:
            description[lang] = ""
        description = MultiLingualString(description, lang)

        aliases = {k: [x["value"] for x in lst] for k, lst in entity["aliases"].items()}
        if lang not in aliases:
            aliases[lang] = []
        aliases = MultiLingualStringList(aliases, lang)
        return WDEntity(
            id=entity["id"].upper(),
            type=entity["type"],
            datatype=entity.get("datatype", None),
            label=label,
            description=description,
            aliases=aliases,
            props=props,
            sitelinks=sitelinks,
        )


@dataclass
class SiteLink:
    __slots__ = ("site", "title", "badges", "url")

    site: str
    title: str
    badges: List[str]
    url: Optional[str]

    def to_dict(self):
        return {
            "site": self.site,
            "title": self.title,
            "badges": self.badges,
            "url": self.url,
        }

    def to_tuple(self):
        return (self.site, self.title, self.badges, self.url)
