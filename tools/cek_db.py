import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

df = pd.read_sql(
    "SELECT * FROM books LIMIT 10",
    engine
)

print(df)