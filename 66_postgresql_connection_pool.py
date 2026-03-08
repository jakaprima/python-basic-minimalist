# TUTORIAL: PostgreSQL Connection Pooling
# Membuka dan menutup koneksi database untuk setiap operasi itu lambat dan boros resource.
# Connection Pool adalah "cache" koneksi yang sudah terbuka dan siap pakai.
# Ini meningkatkan performa dan stabilitas aplikasi secara drastis.

import psycopg2
import psycopg2.pool
import os
import contextlib

# --- KONFIGURASI KONEKSI ---
DB_CONFIG = {
    "dbname": os.getenv("PG_DBNAME", "postgres"),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "your_password"),
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", "5432")
}

# --- 1. Buat Connection Pool (biasanya dibuat sekali saat aplikasi start) ---
# minconn=1: Selalu ada 1 koneksi yang siap.
# maxconn=5: Maksimal 5 koneksi yang bisa dibuka secara bersamaan.
try:
    db_pool = psycopg2.pool.ThreadedConnectionPool(minconn=1, maxconn=5, **DB_CONFIG)
    print("✅ Connection pool berhasil dibuat.")
except psycopg2.OperationalError as e:
    print(f"❌ Gagal membuat connection pool: {e}")
    db_pool = None

# --- 2. Gunakan Context Manager untuk meminjam dan mengembalikan koneksi ---
@contextlib.contextmanager
def get_connection():
    """
    Context manager untuk meminjam koneksi dari pool.
    Otomatis mengembalikan koneksi ke pool setelah selesai, bahkan jika ada error.
    """
    if not db_pool:
        raise IOError("Connection pool tidak tersedia.")
    
    conn = None
    try:
        conn = db_pool.getconn()
        yield conn
    finally:
        if conn:
            db_pool.putconn(conn)

def setup_database():
    """Membuat tabel 'accounts' menggunakan koneksi dari pool."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    balance DECIMAL(10, 2) NOT NULL
                )
            """)
    print("Database dan tabel 'accounts' siap.")

def transfer_funds(from_id, to_id, amount):
    """
    Mentransfer dana menggunakan koneksi dari pool.
    `with get_connection() as conn:` akan memulai transaksi.
    """
    print(f"\n--- Mencoba transfer {amount} dari akun {from_id} ke {to_id} ---")
    try:
        with get_connection() as conn: # Pinjam koneksi dari pool
            with conn.cursor() as cursor:
                cursor.execute("SELECT balance FROM accounts WHERE id = %s FOR UPDATE", (from_id,))
                from_balance = cursor.fetchone()[0]

                if from_balance < amount:
                    raise ValueError("Saldo tidak mencukupi!")

                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, from_id))
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to_id))
        
        print("✅ Transfer berhasil! Koneksi dikembalikan ke pool.")
        return True

    except (Exception, psycopg2.Error) as error:
        print(f"❌ Transfer Gagal! Error: {error}")
        print("Transaksi di-rollback. Koneksi dikembalikan ke pool.")
        return False

def get_all_accounts():
    """Mendapatkan semua data akun untuk verifikasi."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, balance FROM accounts ORDER BY id")
            return cursor.fetchall()

def cleanup():
    """Menghapus tabel dan menutup pool."""
    if db_pool:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS accounts")
        db_pool.closeall()
        print("Tabel 'accounts' di-drop dan semua koneksi di pool ditutup.")

if __name__ == "__main__":
    if not db_pool:
        exit()

    cleanup()
    setup_database()

    # --- Inisialisasi Data ---
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO accounts (name, balance) VALUES ('Alice', 1000.00), ('Bob', 500.00)")
    
    print("\nSaldo Awal:")
    print(get_all_accounts())

    # Skenario 1: Transfer Sukses
    transfer_funds(from_id=1, to_id=2, amount=200.00)
    print("\nSaldo Setelah Transfer Sukses:")
    print(get_all_accounts())

    # Skenario 2: Transfer Gagal (Saldo tidak cukup)
    transfer_funds(from_id=2, to_id=1, amount=1000.00)
    print("\nSaldo Setelah Transfer Gagal (tidak berubah):")
    print(get_all_accounts())

    cleanup()