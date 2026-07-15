# AI-Powered Complaint Management System using Transformer-based NLP

An intelligent complaint management system that leverages state-of-the-art Transformer models to automatically classify complaints, analyze sentiment, generate summaries, detect duplicate complaints, and route them to the appropriate authorities. The application provides an end-to-end workflow for efficient complaint processing through an interactive Streamlit interface.

---

## Features

* Complaint Classification using **BERT**
* Sentiment Analysis using **DistilBERT/RoBERTa**
* Automatic Priority Detection
* Complaint Summarization using **BART**
* Duplicate Complaint Detection using **Sentence-BERT**
* Automatic Authority Routing
* SQLite Database Storage
* Interactive Streamlit Dashboard

---

## System Architecture

```
User Complaint
       │
       ▼
Text Preprocessing
       │
       ▼
BERT Complaint Classification
       │
       ├────────► Sentiment Analysis
       │
       ├────────► Priority Detection
       │
       ├────────► BART Summarization
       │
       ├────────► Sentence-BERT Duplicate Detection
       │
       ▼
Authority Routing
       │
       ▼
SQLite Database
       │
       ▼
Streamlit Dashboard
```

---

## Technologies Used

### Programming Language

* Python

### Deep Learning Framework

* PyTorch

### NLP Libraries

* Hugging Face Transformers
* Sentence Transformers

### Frontend

* Streamlit

### Database

* SQLite

### Development Environment

* VS Code
* Python Virtual Environment

---

## Transformer Models Used

### BERT

* Complaint Classification
* Fine-tuned on a custom complaint dataset

### DistilBERT / RoBERTa

* Sentiment Analysis
* Determines complaint priority

### BART

* Complaint Summarization

### Sentence-BERT

* Duplicate Complaint Detection using cosine similarity

---

## Dataset

The system is trained on a custom dataset containing approximately **840 complaints** distributed across **10 categories**:

* Internet
* Hostel
* Food/Mess
* Transport
* Infrastructure
* Laboratory
* Library
* Administration
* Security
* Electrical

Each record contains:

* Complaint Text
* Category Label

---

## Model Training

| Parameter      | Value             |
| -------------- | ----------------- |
| Base Model     | bert-base-uncased |
| Epochs         | 6                 |
| Batch Size     | 16                |
| Learning Rate  | 2e-5              |
| Optimizer      | AdamW             |
| Training Split | 90%               |
| Testing Split  | 10%               |

---

## Performance

### Classification

* Accuracy: **~89%**
* F1 Score: **~0.87**

### Summarization

* BLEU Score: **0.72**
* ROUGE-1: **0.81**
* ROUGE-2: **0.74**
* ROUGE-L: **0.79**

---

## Example

### Input Complaint

> The hostel WiFi has been terribly slow for the past two days. I can't even load simple websites or send emails. It's making it impossible to complete my online coursework.

### Output

```
Summary:
User reports slow WiFi preventing online coursework.

Category:
Internet

Sentiment:
Negative

Priority:
High

Assigned Authority:
IT Support
```

---

## Project Structure

```
Complaint_Man_Ai/
│
├── app.py
├── train_bert_classifier.py
├── utils.py
├── database.py
├── complaint.db
├── bert_classifier/
├── templates/
├── static/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Complaint_Man_Ai.git
```

Navigate to the project directory:

```bash
cd Complaint_Man_Ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Email and SMS notifications
* Multi-language complaint support
* Voice-based complaint registration
* AI-powered chatbot assistance
* Cloud deployment
* Analytics dashboard
* Role-based authentication
* Mobile application support

---

## References

* BERT – Devlin et al. (2018)
* BART – Lewis et al. (2019)
* Sentence-BERT – Reimers & Gurevych (2019)
* Hugging Face Transformers

---

## Author

**Jignash Geda**

B.Tech Computer Science and Engineering

National Institute of Technology Andhra Pradesh

---

## License

This project is developed for educational and research purposes.
