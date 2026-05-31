import pandas as pd

df = pd.read_csv("dataset/Books.csv")

df["content"] = (
    df["title"].fillna("") + " " +
    df["genre"].fillna("") + " " +
    df["description"].fillna("") + " " +
    df["thumbnail"].fillna("")
)

print(df["content"].head())

print("\nNama Kolom:")
print(df.columns.tolist())