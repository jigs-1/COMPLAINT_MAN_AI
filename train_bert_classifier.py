import pandas as pd
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("combined_college_complaints_dataset.csv")

text_column = "complaint"
label_column = "category"

df = df[[text_column, label_column]]

label_encoder = LabelEncoder()

df["label"] = label_encoder.fit_transform(df[label_column])

dataset = Dataset.from_pandas(df[[text_column, "label"]])


model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)


def tokenize(example):

    return tokenizer(
        example[text_column],
        padding="max_length",
        truncation=True,
        max_length=128
    )


dataset = dataset.map(tokenize)

dataset = dataset.train_test_split(test_size=0.1)

train_dataset = dataset["train"]
test_dataset = dataset["test"]


model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=len(label_encoder.classes_)
)


training_args = TrainingArguments(
    output_dir="./bert_classifier",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=6,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=tokenizer,
)


trainer.train()

model.save_pretrained("bert_classifier")
tokenizer.save_pretrained("bert_classifier")

print("BERT classifier trained successfully.")  