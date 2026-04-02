import os
import sqlite3

# 1. Get the absolute path to the directory where database.py lives (the 'src' folder)
src_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go UP one level to the 'CareerPulse' root folder
root_dir = os.path.dirname(src_dir)

# 3. Define the path to the 'data' folder at the root level
DATA_DIR = os.path.join(root_dir, 'data')
DB_PATH = os.path.join(DATA_DIR, 'career_pulse.db')

# 4. Create the 'data' folder at the root if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

def init_db():
    # Now this ALWAYS points to CareerPulse/data/career_pulse.db
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
    print(f"✅ Database initialized at: {DB_PATH}")

if __name__ == "__main__":
    init_db()