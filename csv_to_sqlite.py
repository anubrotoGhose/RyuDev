import pandas as pd
import sqlite3

# Step 1: Load CSV into a DataFrame
csv_file = 'data/websites.csv'  # Replace with your actual file
df = pd.read_csv(csv_file)

# Step 2: Create SQLite connection
conn = sqlite3.connect('data/programming_knowledge_hub.db')  # Creates a new database file

# Step 3: Write DataFrame to SQLite table
df.to_sql('websites', conn, if_exists='replace', index=False)

# Step 4: Close the connection
conn.close()

print("✅ CSV has been successfully converted to SQLite3!")