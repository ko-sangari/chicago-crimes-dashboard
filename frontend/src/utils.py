import pandas as pd
import httpx


def fetch_data(url):
    result = httpx.get(url)
    df = pd.read_json(result.text)
    return df, len(df)
