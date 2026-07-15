import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Example training data
data = {
    "text": [
        "wifi not working in hostel",
        "internet is very slow",
        "food quality is bad",
        "mess food is terrible",
        "lab computers are not working",
        "library is too noisy",
        "bus arrives late everyday",
        "electricity problem in hostel"
    ],
    
    "category": [
        "Internet",
        "Internet",
        "Food",
        "Food",
        "Laboratory",
        "Library",
        "Transport",
        "Electrical"
    ]
}

df = pd.DataFrame(data)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

y = df["category"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model + vectorizer
joblib.dump(model, "classifier_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully!")