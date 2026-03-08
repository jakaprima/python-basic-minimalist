# TUTORIAL: CRUD Operations with SQLite
# CRUD: Create, Read, Update, Delete.
# `sqlite3` adalah module bawaan Python untuk bekerja dengan database SQLite.
# SQLite tidak butuh server, database-nya hanya sebuah file.

import sqlite3
import os

DB_FILE = "users.db"

def setup_database():
    """Membuat koneksi dan tabel jika belum ada."""
    # `with` statement akan otomatis menangani commit atau rollback jika ada error.
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Gunakan IF NOT EXISTS agar tidak error jika tabel sudah ada
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        print("Database dan tabel 'users' siap.")

# --- CREATE ---
def create_user(name, email):
    """Menambahkan user baru ke database."""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            # Gunakan '?' sebagai placeholder untuk keamanan (mencegah SQL Injection)
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
            print(f"User '{name}' berhasil ditambahkan.")
            return cursor.lastrowid # Mengembalikan ID dari user yang baru dibuat
    except sqlite3.IntegrityError:
        # Terjadi jika kita mencoba memasukkan email yang sudah ada (karena UNIQUE)
        print(f"Error: Email '{email}' sudah ada.")
        return None

# --- READ ---
def get_user_by_id(user_id):
    """Membaca satu user berdasarkan ID."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone() # Mengembalikan satu baris (tuple) atau None

def get_all_users():
    """Membaca semua user dari database."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall() # Mengembalikan list of tuples

# --- UPDATE ---
def update_user_email(user_id, new_email):
    """Mengubah email user berdasarkan ID."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        if cursor.rowcount > 0:
            print(f"Email untuk user ID {user_id} berhasil diubah.")
        else:
            print(f"User dengan ID {user_id} tidak ditemukan.")

# --- DELETE ---
def delete_user(user_id):
    """Menghapus user berdasarkan ID."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        if cursor.rowcount > 0:
            print(f"User dengan ID {user_id} berhasil dihapus.")
        else:
            print(f"User dengan ID {user_id} tidak ditemukan.")

def cleanup():
    """Menghapus file database untuk demo yang bersih."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"File database '{DB_FILE}' dihapus.")

if __name__ == "__main__":
    cleanup()
    
    # 1. Setup
    setup_database()
    
    # 2. CREATE
    print("\n--- CREATE ---")
    user1_id = create_user("Jaka", "jaka@example.com")
    user2_id = create_user("Budi", "budi@example.com")
    create_user("Jaka", "jaka@example.com") # Coba duplikat email, akan gagal

    # 3. READ
    print("\n--- READ (All) ---")
    print(get_all_users())

    # 4. UPDATE
    print("\n--- UPDATE ---")
    update_user_email(user1_id, "jaka.baru@example.com")
    print(f"Data Jaka setelah diupdate: {get_user_by_id(user1_id)}")

    # 5. DELETE
    print("\n--- DELETE ---")
    delete_user(user2_id)
    
    print("\n--- Data Final di Database ---")
    print(get_all_users())

    cleanup()