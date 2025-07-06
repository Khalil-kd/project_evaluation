import pandas as pd
import duckdb
import os

def load_data():
    # chemins vers les fichiers
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    mcd_path = os.path.join(data_dir, "mcd.csv")
    bk_path = os.path.join(data_dir, "bk.csv")

    # initialisation de la base duckdb en mémoire
    con = duckdb.connect(database=':memory:')

    # création des tables
    con.execute(f"CREATE TABLE mcd AS SELECT * FROM read_csv_auto('{mcd_path}')")
    con.execute(f"CREATE TABLE bk AS SELECT * FROM read_csv_auto('{bk_path}')")

    return con

def show_schema(con):
    print("Schema MCD :")
    print(con.sql("PRAGMA table_info('mcd')").df())
    print("\nSchema BK :")
    print(con.sql("PRAGMA table_info('bk')").df())

def show_preview(con):
    print("\nAperçu des 5 premières lignes de MCD :")
    print(con.sql("SELECT * FROM mcd LIMIT 5").df())

    print("\nAperçu des 5 premières lignes de BK :")
    print(con.sql("SELECT * FROM bk LIMIT 5").df())

if __name__ == "__main__":
    con = load_data()
    show_schema(con)
    show_preview(con)
