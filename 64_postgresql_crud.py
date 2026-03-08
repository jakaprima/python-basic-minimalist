# TUTORIAL: CRUD Operations with PostgreSQL
# CRUD: Create, Read, Update, Delete.
# Untuk PostgreSQL, kita butuh library eksternal. Yang paling populer adalah `psycopg2`.
# Install dulu: pip install psycopg2-binary

import psycopg2
import psycopg2.errors
import os

# --- KONFIGURASI KONEKSI ---
# Ganti dengan detail koneksi database PostgreSQL Anda.
# Untuk demo ini, kita bisa menggunakan environment variables agar lebih aman.
DB_CONFIG = {
    "dbname": os.getenv("PG_DBNAME", "postgres"),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "your_password"),
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", "5432")
}

def setup_database():
    """Membuat koneksi dan tabel jika belum ada."""
    # `with` statement akan otomatis menangani commit atau rollback jika ada error.
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            # SERIAL adalah tipe data auto-increment di PostgreSQL
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE
                )
            """)
    print("Database dan tabel 'users' siap.")

# --- CREATE ---
def create_user(name, email):
    """Menambahkan user baru ke database."""
    sql = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;"
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # Gunakan '%s' sebagai placeholder untuk psycopg2
                cursor.execute(sql, (name, email))
                new_id = cursor.fetchone()[0] # Ambil ID yang dikembalikan oleh RETURNING
                print(f"User '{name}' dengan ID {new_id} berhasil ditambahkan.")
                return new_id
    except psycopg2.errors.UniqueViolation:
        print(f"Error: Email '{email}' sudah ada.")
        return None
    except psycopg2.OperationalError as e:
        print(f"Koneksi Gagal: {e}")
        return None

# --- READ ---
def get_user_by_id(user_id):
    """Membaca satu user berdasarkan ID."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            return cursor.fetchone()

def get_all_users():
    """Membaca semua user dari database."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

# --- UPDATE ---
def update_user_email(user_id, new_email):
    """Mengubah email user berdasarkan ID."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
            if cursor.rowcount > 0:
                print(f"Email untuk user ID {user_id} berhasil diubah.")
            else:
                print(f"User dengan ID {user_id} tidak ditemukan.")

# --- DELETE ---
def delete_user(user_id):
    """Menghapus user berdasarkan ID."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
            if cursor.rowcount > 0:
                print(f"User dengan ID {user_id} berhasil dihapus.")
            else:
                print(f"User dengan ID {user_id} tidak ditemukan.")

def cleanup():
    """Menghapus tabel untuk demo yang bersih."""
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS users")
        print("Tabel 'users' telah di-drop.")
    except psycopg2.OperationalError as e:
        print(f"Tidak bisa cleanup, koneksi gagal: {e}")

if __name__ == "__main__":
    # Pastikan Anda sudah mengganti detail koneksi di DB_CONFIG
    # atau mengatur environment variables.
    cleanup()
    setup_database()

    print("\n--- CREATE ---")
    user1_id = create_user("Wanda", "wanda@pgsql.com")
    user2_id = create_user("Vision", "vision@pgsql.com")

    print("\n--- READ (All) ---")
    print(get_all_users())

    print("\n--- UPDATE ---")
    if user1_id:
        update_user_email(user1_id, "wanda.maximoff@pgsql.com")
        print(f"Data Wanda setelah diupdate: {get_user_by_id(user1_id)}")

    print("\n--- DELETE ---")
    if user2_id:
        delete_user(user2_id)

    print("\n--- Data Final di Database ---")
    print(get_all_users())

    cleanup()