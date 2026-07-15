from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_complaint(text):

    summary = summarizer(
        text,
        max_length=30,
        min_length=10,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    return summary[0]["summary_text"]