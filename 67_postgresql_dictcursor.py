# TUTORIAL: Mengembalikan Baris Database sebagai Dictionary (DictCursor)
# Secara default, psycopg2 mengembalikan baris data sebagai tuple.
# Ini cepat, tapi kurang deskriptif karena kita harus mengakses data via index (misal: row[1]).
# Dengan `DictCursor`, kita bisa mendapatkan baris sebagai dictionary-like object,
# sehingga bisa diakses dengan nama kolom (misal: row['name']).

import psycopg2
import psycopg2.extras # Import extras module
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
    """Membuat dan mengisi tabel 'products' untuk demo."""
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS products;")
                cursor.execute("""
                    CREATE TABLE products (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(255) NOT NULL,
                        price DECIMAL(10, 2) NOT NULL
                    )
                """)
                cursor.execute("""
                    INSERT INTO products (name, price) VALUES
                    ('Laptop', 1500.00),
                    ('Mouse', 25.50)
                """)
        print("Database dan tabel 'products' siap.")
    except psycopg2.OperationalError as e:
        print(f"Koneksi Gagal: {e}")
        exit()

# --- 1. Cara Default: Menggunakan Tuple ---
def read_as_tuples():
    """Membaca data dan mengembalikannya sebagai list of tuples."""
    print("\n--- 1. Membaca sebagai Tuple (Default) ---")
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, name, price FROM products")
            products = cursor.fetchall()
            
            print(f"Tipe data baris pertama: {type(products[0])}")
            # Mengakses data dengan index, kurang deskriptif
            for row in products:
                print(f"ID: {row[0]}, Nama: {row[1]}, Harga: {row[2]}")

# --- 2. Cara Modern: Menggunakan Dictionary (DictCursor) ---
def read_as_dicts():
    """Membaca data dan mengembalikannya sebagai list of dictionary-like objects."""
    print("\n--- 2. Membaca sebagai Dictionary (DictCursor) ---")
    with psycopg2.connect(**DB_CONFIG) as conn:
        # Gunakan `cursor_factory` untuk mengubah perilaku cursor
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT id, name, price FROM products")
            products = cursor.fetchall()

            print(f"Tipe data baris pertama: {type(products[0])}")
            # Mengakses data dengan nama kolom, lebih mudah dibaca dan aman
            for row in products:
                print(f"ID: {row['id']}, Nama: {row['name']}, Harga: {row['price']}")

if __name__ == "__main__":
    setup_database()
    read_as_tuples()
    read_as_dicts()
    # Cleanup
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS products")
    print("\nTabel 'products' telah di-drop.")