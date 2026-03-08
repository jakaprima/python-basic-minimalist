# TUTORIAL: Context Managers dan Statement `with`
# Context Manager bertugas mengelola resource (setup dan teardown) secara otomatis.
# Contoh paling umum adalah `with open(...)`, yang otomatis menutup file setelah selesai.

from contextlib import contextmanager
import os
import time

# --- 1. Cara Kerja `with` ---
# Statement `with` menjamin bahwa resource dibersihkan (cleanup)
# meskipun terjadi error di tengah blok kode.

# Tanpa `with` (Manual & Berisiko):
# f = open("test.txt", "w")
# try:
#     f.write("Halo")
# finally:
#     f.close() # Harus ingat close()

# Dengan `with` (Otomatis):
# with open("test.txt", "w") as f:
#     f.write("Halo")
# (File otomatis ditutup di sini)


# --- 2. Membuat Context Manager Sendiri (Class Based) ---
# Kita harus mengimplementasikan method spesial `__enter__` dan `__exit__`.

class FileManagerCustom:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Dijalankan saat masuk blok `with`
        print(f"--- [Class] Membuka file: {self.filename} ---")
        self.file = open(self.filename, self.mode)
        return self.file # Nilai ini yang masuk ke variabel `as ...`

    def __exit__(self, exc_type, exc_value, traceback):
        # Dijalankan saat keluar blok `with` (selesai atau error)
        print(f"--- [Class] Menutup file: {self.filename} ---")
        if self.file:
            self.file.close()
        
        # Handle Exception
        if exc_type:
            print(f"    Terjadi Error: {exc_value}")
            # Return True jika ingin menelan error (program tidak crash)
            # Return False (atau None) jika ingin error tetap di-raise ke luar
            return True 

print("1. Demo Class-Based Context Manager:")
with FileManagerCustom("test_context.txt", "w") as f:
    f.write("Ini ditulis dari Class Context Manager")
    # raise ValueError("Ups error buatan!") # Coba uncomment ini untuk tes handling error


# --- 3. Membuat Context Manager dengan Decorator (Generator Based) ---
# Cara lebih ringkas menggunakan module `contextlib`.
# Sangat berguna jika tidak butuh menyimpan state yang kompleks dalam class.

@contextmanager
def timer_context():
    start = time.time()
    print("\n--- [Func] Timer Mulai ---")
    
    try:
        yield # Kode di dalam blok `with` dijalankan di titik ini
    finally:
        # Kode ini dijalankan setelah blok `with` selesai (mirip __exit__)
        end = time.time()
        print(f"--- [Func] Timer Selesai. Waktu: {end - start:.4f} detik ---")

print("\n2. Demo Generator-Based Context Manager:")
with timer_context():
    print("   Sedang memproses data berat...")
    time.sleep(0.5) # Simulasi proses

# Cleanup file sisa
if os.path.exists("test_context.txt"):
    os.remove("test_context.txt")