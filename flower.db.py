import sqlite3

conn = sqlite3.connect('flower.db')
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
print('Flowers table created successfully.')