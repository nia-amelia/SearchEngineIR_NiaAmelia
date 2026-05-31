import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

# baca csv
df = pd.read_csv("dataset/Books.csv")

with engine.begin() as conn:

    for index, row in df.iterrows():

        conn.execute(
            text("""
                UPDATE books
                SET thumbnail = :thumbnail
                WHERE title = :title
            """),
            {
                "thumbnail": str(row["thumbnail"]),
                "title": str(row["title"])
            }
        )

print("Thumbnail berhasil diupdate!")