import sqlite3
import pandas as pd

DB_PATH = "data/traffic.db"
CSV_PATH = "data/processed/traffic_metrics.csv"


def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS traffic_metrics (
        time INTEGER,
        avg_velocity REAL,
        num_cars INTEGER,
        congestion_index REAL,
        traffic_level TEXT
    );
    """
    conn.execute(query)
    conn.commit()


def load_data(conn):
    df = pd.read_csv(CSV_PATH)
    df.to_sql("traffic_metrics", conn, if_exists="replace", index=False)
    print("Datos cargados a la base de datos")


def main():
    conn = create_connection()
    create_table(conn)
    load_data(conn)
    conn.close()


if __name__ == "__main__":
    main()
