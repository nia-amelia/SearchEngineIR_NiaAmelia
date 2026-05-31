from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:rizqiputra@localhost:5432/SearchEngineIR"
)

conn = engine.connect()

print("Koneksi berhasil!")

conn.close()