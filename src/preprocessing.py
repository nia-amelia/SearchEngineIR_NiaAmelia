import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# stopword bahasa Inggris
stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = str(text)

    # lowercase
    text = text.lower()

    # hapus karakter selain huruf dan angka
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # tokenisasi
    tokens = word_tokenize(text)

    # hapus stopword
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

# tampilkan 5 data pertama

for i in range(5):

    print("\n========================")
    print("ASLI:")
    print(df["content"][i][:300])

    print("\nHASIL:")
    print(df["processed"][i][:300])