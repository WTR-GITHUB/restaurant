import sqlite3

conn = sqlite3.connect("restaurant.db")
c = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS "menu" (
    "category"	TEXT,
	"Category_ID"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("Category_ID" AUTOINCREMENT)
);
"""

with conn:
    c.execute(query)
