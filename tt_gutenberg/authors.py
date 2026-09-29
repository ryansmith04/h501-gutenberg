from .transform import get_data


def list_authors(by_languages=True, alias=True):
    data = get_data()
    language_counts = (
        data.groupby("gutenberg_author_id")["language"]
        .nunique()
        .reset_index(name="language_count")
    )
    authors = data[
        [
            "gutenberg_author_id",
            "author",
            "alias",
        ]
    ].drop_duplicates()
    authors = authors.merge(
        language_counts,
        on="gutenberg_author_id",
        how="left",
    )

    if by_languages:
        authors = authors.sort_values(
            "language_count",
            ascending=False,
        )
    if alias:
        return authors["alias"].dropna().tolist()
    return authors["author"].dropna().tolist()
