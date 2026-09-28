from .data import load_authors, load_metadata


def list_authors(by_languages=True, alias=True):
    authors = load_authors()
    metadata = load_metadata()

    language_counts = (
        metadata.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="language_count")
    )

    authors = authors.merge(
        language_counts,
        on="gutenberg_author_id",
        how="left",
    )

    if by_languages:
        authors = authors.sort_values("language_count", ascending=False)
    
    if alias:
        return authors["alias"].dropna().tolist()

    return authors["author"].tolist()
