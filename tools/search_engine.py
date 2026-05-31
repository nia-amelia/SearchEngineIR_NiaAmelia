import pandas as pd
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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


# ==========================
# QUERY USER
# ==========================

query = input("Search book: ")

query_processed = preprocess(query)

query_vector = vectorizer.transform([query_processed])


# ==========================
# COSINE SIMILARITY
# ==========================

similarity = cosine_similarity(
    query_vector,
    tfidf_matrix
)

scores = similarity.flatten()

df["score"] = scores


# ==========================
# TOP 5 HASIL
# ==========================

results = df[df["score"] > 0]
results = df.sort_values(
    by="score",
    ascending=False
).head(5)
if results.empty:
    print("\nTidak ada buku yang cocok.")
else:

    print("\n===== SEARCH RESULTS =====\n")

    for _, row in results.iterrows():

        print("Title :", row["title"])
        print("Author:", row["author"])
        print("Genre :", row["genre"])
        print("Score :", round(row["score"], 4))
        print("-" * 50)
