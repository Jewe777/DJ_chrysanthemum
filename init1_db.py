import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'shop.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
''')

# Optional: Insert sample data if table is empty
cursor.execute("SELECT COUNT(*) FROM flowers")
if cursor.fetchone()[0] == 0:
    flowers = [
    ('Spider Chrysanthemum', 50, 'spider.jpg'),
    ('Pompon Chrysanthemum', 45, 'pompon.jpg'),
    ('Spoon Chrysanthemum', 55, 'spoon.jpg'),
    ('Quill Chrysanthemum', 60, 'quill.jpg'),
    ('Brush and Thistle Chrysanthemum', 50, 'brush.jpg'),
    ('Anemone Chrysanthemum', 65, 'anemone.jpg'),
    ('Single and Semi-Double Chrysanthemum', 40, 'single.jpg'),
    ('Intermediate Incurve Chrysanthemum', 70, 'intermediate.jpg'),
    ('Decorative Chrysanthemum', 75, 'decorative.jpg'),
    ('Regular Incurve Chrysanthemum', 80, 'regular.jpg'),
    ('Reflex Chrysanthemum', 65, 'reflex.jpg'),
    ('Irregular Incurve Chrysanthemum', 85, 'irregular.jpg'),

    ]
    cursor.executemany("INSERT INTO flowers (name, price, image) VALUES (?, ?, ?)", flowers)

conn.commit()
conn.close()

print("✅ shop.db is ready with flowers table and sample data.")
