import pandas as pd

from . import DATA


def load_table(kind):
    """Find the DATA entry whose key mentions `kind` and return it as a DataFrame."""
    for key, value in DATA.items():
        if kind in str(key).lower():
            if isinstance(value, pd.DataFrame):
                return value.copy()
            return pd.read_csv(value)
    raise KeyError(f"No entry for '{kind}' in DATA. Keys are: {list(DATA)}")


def get_data():
    """Merge the Gutenberg metadata with the authors table."""
    authors = load_table("author")
    metadata = load_table("metadata")
    # if both tables have an 'author' column, keep the one from authors
    if "author" in metadata.columns and "author" in authors.columns:
        metadata = metadata.drop(columns=["author"])
    df = metadata.merge(authors, on="gutenberg_author_id", how="inner")
    if "alias" in df.columns:
        df["author_alias"] = df["alias"]
    return df


def count_languages(df, by="author_alias"):
    """Number of distinct languages per group, sorted high to low."""
    langs = df.dropna(subset=[by, "language"]).copy()
    langs["language"] = langs["language"].astype(str).str.split("/")
    langs = langs.explode("language")
    return langs.groupby(by)["language"].nunique().sort_values(ascending=False, kind="stable")
