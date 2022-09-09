#!/usr/bin/env python3

from typing import List
from papis.document import Document, to_dict


def to_authors(author_list: List[dict]) -> str:
    if len(author_list) < 1:
        return ""

    key = ""
    if "surname" in author_list[0].keys():
        key = "surname"
    elif "family" in author_list[0].keys():
        key = "family"

    if len(author_list) > 3:
        surname = author_list[0][key] or "" 
        return surname + " et. al."
    else:
        return ", ".join([author[key] or "" for author in author_list])


def to_bibliography(document: dict) -> str:
    year = document["year"] or ""
    authors = to_authors(document["author_list"]) or ""
    title = document["title"] or ""
    doi_or_isbn = ""
    if "doi" in document.keys():
        doi_or_isbn = "doi: " + document["doi"]
    if "DOI" in document.keys():
        doi_or_isbn = "doi: " + document["DOI"]
    elif "isbn" in document.keys():
        doi_or_isbn = "isbn: " + document["isbn"]
    elif "ISBN" in document.keys():
        doi_or_isbn = "isbn: " + document["ISBN"]
    bibliography = "{year}; {authors}; \"{title}\"; {doi_or_isbn}".format(
        year = year,
        authors = authors,
        title = title,
        doi_or_isbn = doi_or_isbn,
    )
    return bibliography


def exporter(documents: List[Document]) -> str:
    docs_dict = [to_dict(document) for document in documents]
    bibliographies = map(to_bibliography, docs_dict)
    return "\n".join(bibliographies)
