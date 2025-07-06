import duckdb
import os

def load_data():
    con = duckdb.connect(database=':memory:')
    mcd_path = os.path.join("data", "mcd.csv")
    bk_path = os.path.join("data", "bk.csv")

    con.execute(f"CREATE TABLE mcd AS SELECT * FROM read_csv_auto('{mcd_path}')")
    con.execute(f"CREATE TABLE bk AS SELECT * FROM read_csv_auto('{bk_path}')")

    return con
