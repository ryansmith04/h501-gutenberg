from .data import load_authors, load_metadata


def get_data():
    authors = load_authors()
    metadata = load_metadata()
    metadata = metadata.drop(columns=["author"])
    return authors.merge(
        metadata,
        on="gutenberg_author_id",
        how="left",
    )