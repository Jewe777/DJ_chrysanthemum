import sqlite3

conn = sqlite3.connect('shop.db')
c = conn.cursor()

# Add image column to shop_items if not already added
c.execute("ALTER TABLE shop_items ADD COLUMN image TEXT")

conn.commit()
conn.close()

print("✅ 'image' column added to shop_items table.")
