import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/techflow_support.db"

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM support_calls"

df = pd.read_sql(query, engine)

df.to_csv("exports/support_calls.csv", index=False)

print("CSV export completed successfully.")