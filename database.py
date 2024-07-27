import sqlite3
from datetime import datetime

DATABASE = 'inventory.db'

def database():
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS products (
              id TEXT PRIMARY KEY,
              name TEXT,
              price REAL,
              quantity INTEGER
          )
      ''')
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS cart (
              id TEXT PRIMARY KEY,
              name TEXT,
              price REAL,
              quantity INTEGER
          )
      ''')
        cursor.execute('''
          CREATE TABLE IF NOT EXISTS sales (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              product_id TEXT,
              product_name TEXT,
              sold_quantity INTEGER,
              sale_date TEXT
          )
      ''')

        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

    finally:
        conn.close()

def execute_db_query(query, params=()):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        if query.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE')):
            conn.commit()
        else:
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        conn.close()

def fetch_db_query(query, params=()):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return rows
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

database()