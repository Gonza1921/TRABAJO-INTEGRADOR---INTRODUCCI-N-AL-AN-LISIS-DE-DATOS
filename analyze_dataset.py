import pandas as pd
import sqlite3
import os

# Load dataset
df = pd.read_csv('Student_performance_CLEANED.csv')

print('Total rows:', len(df))
print('Columns:', len(df.columns))
print('Columns:', list(df.columns))

# Basic statistics
print('\nBasic Statistics:')
print(df.describe())

# Check data quality
print('\nMissing values:')
print(df.isnull().sum())

# Check unique values for key columns
print('\nUnique values:')
for col in ['gender', 'race_ethnicity', 'grade', 'lunch', 'test_preparation_course']:
    if col in df.columns:
        print(f'{col}: {df[col].nunique()} unique values')
        print(f'  Sample: {df[col].unique()[:5]}')

# Create SQLite database
print('\nCreating SQLite database...')
conn = sqlite3.connect('academico.db')

# Create estudiantes table
df.to_sql('estudiantes', conn, if_exists='replace', index=False)

# Verify data was loaded
result = pd.read_sql('SELECT COUNT(*) as count FROM estudiantes', conn)
print(f'\nRecords in SQLite: {result["count"].iloc[0]}')

# Show table schema
print('\nTable schema:')
result = pd.read_sql("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='estudiantes'", conn)
print(result['sql'].iloc[0])

conn.close()
print('\n✅ SQLite database created successfully!')