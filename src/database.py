import sqlite3

def init_db( ):
	conn = sqlite3.connect('career_pulse.db')
	c = conn.cursor()

	c.execute("""
		CREATE TABLE IF NOT EXISTS urls (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				original_url TEXT NOT NULL,
				short_code TEXT UNIQUE NOT NULL,
				created_at DATETIME DEFAULT CURRENT_TIMESTAMP
		)
	""")

	conn.commit() # Save the changes
	conn.close() # Close the connection

# 1. Database initialization verification

if __name__ == "__main__":
	init_db()
	print("✅ CareerPulse Database Initialized!")