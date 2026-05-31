import pandas as pd
import re

from sqlalchemy import create_engine

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


import nltk

nltk.download("punkt")
nltk.download("stopwords")

# ==========================
# PREPROCESSING
# ==========================

stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)


# ==========================
# BACA DATASET
# ==========================

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

engine = create_engine(DATABASE_URL)

df = pd.read_sql(
    "SELECT * FROM books",
    engine
)

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
    ).head(5)

    return results