from .transform import get_data, count_languages


def list_authors(by_languages=True, alias=True):
    """List authors (or aliases) ordered by translation count."""
    df = get_data()
    if alias:
        col = "author_alias" if "author_alias" in df.columns else "alias"
    else:
        col = "author"
    if by_languages:
        counts = count_languages(df, by=col)
    else:
        counts = df.dropna(subset=[col]).groupby(col)["gutenberg_id"].nunique() \
                   .sort_values(ascending=False, kind="stable")
    return counts.index.tolist()
