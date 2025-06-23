import sqlite3

conn = sqlite3.connect('shop.db')  # Use your actual DB filename here
cursor = conn.cursor()

# Create the flowers table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS flowers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    image TEXT
)
''')

# List of flower data as tuples (name, price, description, image)
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

# Insert multiple rows using executemany
cursor.executemany(
    "INSERT INTO flowers (name, price, image) VALUES (?, ?, ?)",
    flowers
)

conn.commit()
conn.close()

print("Database initialized with flowers table and sample data.")
