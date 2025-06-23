import sqlite3

conn = sqlite3.connect('dj_chrysanthemum.db')  # Use your actual DB file
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
''')

conn.commit()
conn.close()

print("Table 'flowers' created successfully.")
