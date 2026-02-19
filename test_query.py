import sqlite3
import pandas as pd

conn = sqlite3.connect("data/traffic.db")

query = "SELECT * FROM traffic_metrics LIMIT 5;"
df = pd.read_sql(query, conn)

print(df)
