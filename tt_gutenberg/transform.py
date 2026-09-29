from . import DATA
from .data import load_authors, load_metadata


def get_data():
    authors = load_authors(DATA["authors"])
    metadata = load_metadata(DATA["metadata"])
    metadata = metadata.drop(columns=["author"], errors="ignore")
    return authors.merge(
        metadata,
        on="gutenberg_author_id",
        how="inner")
