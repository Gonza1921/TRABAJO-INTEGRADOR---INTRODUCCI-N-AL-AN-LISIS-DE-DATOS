import pandas as pd
import sqlite3

# Load the data
df = pd.read_csv('Student_performance_CLEANED.csv')

# Create SQLite connection
conn = sqlite3.connect('academico.db')

# Create the estudiantes table
df.to_sql('estudiantes', conn, if_exists='replace', index=False)

# Verify the data was loaded
result = pd.read_sql('SELECT COUNT(*) as count FROM estudiantes', conn)
print(f"[OK] SQLite database created successfully with {result['count'].iloc[0]} records")

conn.close()