import sqlite3

connection = sqlite3.connect("iiot_project.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL
)
""")

connection.commit()
print("✅ Database and table created!")

connection.close()
