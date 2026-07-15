from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sqlite3


model = SentenceTransformer("all-MiniLM-L6-v2")


def check_duplicate(new_complaint):

    conn = sqlite3.connect("complaints.db")
    cursor = conn.cursor()

    cursor.execute("SELECT complaint FROM complaints")

    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        return False

    complaints = [r[0] for r in rows]

    embeddings = model.encode(complaints + [new_complaint])

    new_vec = embeddings[-1]
    existing_vecs = embeddings[:-1]

    scores = cosine_similarity([new_vec], existing_vecs)[0]

    max_score = max(scores)

    if max_score > 0.75:
        return True

    return False