from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

def get_sentiment(text):

    result = sentiment_pipeline(text)[0]

    label = result["label"]

    if label == "LABEL_0":
        return "Negative"

    elif label == "LABEL_1":
        return "Neutral"

    else:
        return "Positive"


def get_priority_from_sentiment(sentiment):

    if sentiment == "Negative":
        return "High"

    elif sentiment == "Neutral":
        return "Medium"

    else:
        return "Low"