import pandas as pd
from sqlalchemy import create_engine

# koneksi database
engine = create_engine(
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

# baca csv
df = pd.read_csv("dataset/Books.csv")

# ambil kolom yang dipakai
df = df[
    [
        "title",
        "author",
        "genre",
        "description"
    ]
]

# simpan ke postgresql
df.to_sql(
    "books",
    engine,
    if_exists="append",
    index=False
)

print("Import berhasil!")