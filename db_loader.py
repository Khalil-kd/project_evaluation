import duckdb
import os

def load_combined_data():
    con = duckdb.connect(database=':memory:')

    mcd_path = os.path.join("data", "mcd.csv")
    bk_path = os.path.join("data", "bk.csv")

    con.execute(f"CREATE TABLE mcd AS SELECT * FROM read_csv_auto('{mcd_path}')")
    con.execute(f"CREATE TABLE bk AS SELECT * FROM read_csv_auto('{bk_path}')")

    combined_query = """
        SELECT 
            table_name,
            heading,
            item,
            Date,
            Value,
            'mcd' AS restaurant
        FROM mcd

        UNION ALL

        SELECT 
            NULL AS table_name,
            Attribute AS heading,
            item,
            DATE_TRUNC('year', MAKE_DATE(CAST(Attribute AS INTEGER), 1, 1)) AS Date,
            Value,
            'bk' AS restaurant
        FROM bk
    """

    combined_df = con.sql(combined_query).df()
    return con, combined_df

