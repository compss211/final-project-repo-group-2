import pandas as pd
import re


def clean_text(text):
    """
    Clean text by removing special characters, converting to lowercase, etc.
    """
    if pd.isna(text):
        return ""
    text = text.lower()  # convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra whitespace
    cleaned = text
    return cleaned



def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'