import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

df = pd.read_sql(
    "SELECT title, thumbnail FROM books LIMIT 5",
    engine
)

print(df)