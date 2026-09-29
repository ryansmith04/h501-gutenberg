from . import transform


def list_authors(by_languages=True, alias=True):
    """List authors (or aliases) ordered by translation count."""
    df = transform.get_data()
    col = "alias" if alias else "author"
    if by_languages:
        counts = transform.count_languages(df, by=col)
    else:
        counts = df.dropna(subset=[col]).groupby(col)["gutenberg_id"].nunique() \
                   .sort_values(ascending=False, kind="stable")
    return counts.index.tolist()
