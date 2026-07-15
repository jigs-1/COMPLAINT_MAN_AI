import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

MODEL_PATH = "bert_classifier"


@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

    df = pd.read_csv("combined_college_complaints_dataset.csv")
    labels = sorted(df["category"].unique().tolist())

    return tokenizer, model, labels


tokenizer, model, labels = load_model()


def predict_category(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    probabilities = torch.softmax(logits, dim=1)[0]

    # top 3 predictions
    top3 = torch.topk(probabilities, 3)

    predictions = []

    for score, idx in zip(top3.values, top3.indices):

        label = labels[idx]

        predictions.append(
            (label, float(score))
        )

    category = predictions[0][0]

    confidence = predictions[0][1]

    return category, confidence, predictions