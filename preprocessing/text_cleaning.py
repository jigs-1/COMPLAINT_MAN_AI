import re


def clean_text(text):

    text = text.lower()

    # remove urls
    text = re.sub(r"http\S+", "", text)

    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text