# TUTORIAL: Transaksi pada Operasi CRUD PostgreSQL
# Transaksi adalah serangkaian operasi yang diperlakukan sebagai satu unit kerja tunggal.
# Prinsipnya "all or nothing": jika satu langkah gagal, semua langkah sebelumnya dibatalkan (rollback).
# Ini penting untuk menjaga konsistensi data.

import psycopg2
import psycopg2.errors
import os

# --- KONFIGURASI KONEKSI ---
DB_CONFIG = {
    "dbname": os.getenv("PG_DBNAME", "postgres"),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "your_password"),
    "host": os.getenv("PG_HOST", "localhost"),
    "port": os.getenv("PG_PORT", "5432")
}

def setup_database():
    """Membuat tabel 'accounts' untuk demo transaksi."""
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS accounts (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        balance DECIMAL(10, 2) NOT NULL
                    )
                """)
        print("Database dan tabel 'accounts' siap.")
    except psycopg2.OperationalError as e:
        print(f"Koneksi Gagal: {e}")
        # Keluar jika database tidak bisa disiapkan
        exit()

def transfer_funds(from_id, to_id, amount):
    """
    Mentransfer dana antar akun dalam satu transaksi atomik.
    Jika salah satu langkah gagal, semua perubahan akan dibatalkan.
    """
    print(f"\n--- Mencoba transfer {amount} dari akun {from_id} ke {to_id} ---")
    try:
        # `with` block ini mengelola seluruh transaksi.
        # Jika block selesai tanpa error, `conn.commit()` akan dipanggil otomatis.
        # Jika ada error (misal ValueError), `conn.rollback()` akan dipanggil otomatis.
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                # 1. Ambil saldo pengirim
                cursor.execute("SELECT balance FROM accounts WHERE id = %s", (from_id,))
                from_balance = cursor.fetchone()[0]

                # 2. Validasi saldo
                if from_balance < amount:
                    raise ValueError("Saldo tidak mencukupi!")

                # 3. Kurangi saldo pengirim
                cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id = %s", (amount, from_id))
                
                # 4. Tambah saldo penerima
                cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id = %s", (amount, to_id))
        
        print("✅ Transfer berhasil!")
        return True

    except (Exception, psycopg2.Error) as error:
        print(f"❌ Transfer Gagal! Error: {error}")
        print("Transaksi di-rollback. Tidak ada saldo yang berubah.")
        return False

def get_all_accounts():
    """Mendapatkan semua data akun untuk verifikasi."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, balance FROM accounts ORDER BY id")
            return cursor.fetchall()

def cleanup():
    """Menghapus tabel untuk demo yang bersih."""
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS accounts")
    print("Tabel 'accounts' telah di-drop.")

if __name__ == "__main__":
    cleanup()
    setup_database()

    # --- Inisialisasi Data ---
    with psycopg2.connect(**DB_CONFIG) as conn:
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