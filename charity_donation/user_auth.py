import sqlite3
from .db_connection import get_db_connection
from .data_models import User

logged_in_user = None

def register_user(username, email, password, full_name):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password, full_name) VALUES (?, ?, ?, ?)",
              (username, email, password, full_name))
    conn.commit()
    conn.close()
    print("User registered successfully!")

def login_user(username, password):
    global logged_in_user
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    row = c.fetchone()
    conn.close()
    if row:
        logged_in_user = User(row["id"], row["username"], row["email"], row["password"], row["full_name"])
        print(f"Welcome {logged_in_user.full_name}!")
        return True
    else:
        print("Login failed. Check username and password.")
        return False

def logout_user():
    global logged_in_user
    logged_in_user = None
    print("Logged out successfully.")

def get_current_user():
    return logged_in_user
