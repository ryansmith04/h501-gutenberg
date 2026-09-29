import pandas as pd


def load_authors(url):
    return pd.read_csv(url)


def load_metadata(url):
    return pd.read_csv(url)
