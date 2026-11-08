import sqlite3

# Intentionally insecure: SQL injection vulnerability
def get_user_unsafe(username):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


# Secure: Parameterized SQL query
def get_user_safe(username):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    return cursor.fetchall()


# Intentionally insecure: Hardcoded secret
API_KEY = "TEST_ONLY_INSECURE_KEY_123456"

# Secure alternative: Read secret from environment
import os
SECURE_API_KEY = os.getenv("API_KEY")
