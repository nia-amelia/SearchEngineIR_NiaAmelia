import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================
# PREPROCESSING
# ==========================

stop_words = {
    "a","an","the","and","or","but",
    "is","are","was","were","be","been",
    "in","on","at","to","for","of",
    "with","by","from","that","this",
    "it","as","not","have","has","had",
    "will","would","can","could","should"
}

def preprocess(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    tokens = text.split()

    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)


# ==========================
# BACA DATASET
# ==========================

df = pd.read_csv("dataset/Books.csv")

df["content"] = (
    df["title"].fillna("") + " " +
    df["genre"].fillna("") + " " +
    df["description"].fillna("")
)

df["processed"] = df["content"].apply(preprocess)


# ==========================
# TF-IDF
# ==========================

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(df["processed"])

def search_books(query):

    query_processed = preprocess(query)

    query_vector = vectorizer.transform(
        [query_processed]
    )

    similarity = cosine_similarity(
        query_vector,
        tfidf_matrix
    )

    scores = similarity.flatten()

    df["score"] = scores

    results = df[df["score"] > 0]

    results = results.sort_values(
    by="score",
    ascending=False
    )

    return results