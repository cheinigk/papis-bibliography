#!/usr/bin/env python3

from typing import List
from papis.document import Document, to_dict


def to_authors(author_list: List[dict]) -> str:
    if len(author_list) > 3:
        return author_list[0]["surname"] + " et. al."
    else:
        return ", ".join([author["surname"] for author in author_list[0:3]])


def to_bibliography(document: dict) -> str:
    year = document["year"]
    authors = to_authors(document["author_list"])
    title = document["title"]
    doi = document["doi"]
    bibliography = "{year}; {authors}; \"{title}\"; doi: {doi}".format(
        year = year,
        authors = authors,
        title = title,
        doi = doi,
    )
    return bibliography


def exporter(documents: List[Document]) -> str:
    docs_dict = [to_dict(document) for document in documents]
    bibliographies = map(to_bibliography, docs_dict)
    return "\n".join(bibliographies)
