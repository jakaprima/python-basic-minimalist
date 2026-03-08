# TUTORIAL: Generators dan Keyword `yield`
# Generator adalah cara membuat iterator dengan mudah.
# Berbeda dengan function biasa yang mengembalikan nilai sekaligus (return),
# generator menghasilkan nilai satu per satu (yield) dan "mengingat" posisi terakhirnya.

import sys

# --- 1. Konsep Dasar: Return vs Yield ---

def fungsi_biasa():
    """Mengembalikan semua data sekaligus (memakan memori)."""
    return [1, 2, 3]

def fungsi_generator():
    """Mengembalikan data satu per satu (hemat memori)."""
    yield 1
    yield 2
    yield 3

print("--- 1. Basic Usage ---")
gen = fungsi_generator()
print(f"Object Generator: {gen}")

# Kita bisa mengambil nilai menggunakan next() secara manual
print(f"Output 1: {next(gen)}") # Output: 1
print(f"Output 2: {next(gen)}") # Output: 2
print(f"Output 3: {next(gen)}") # Output: 3
# print(next(gen)) # Jika dipanggil lagi, akan raise StopIteration Error

# --- 2. State Retention (Mengingat Posisi) ---
# Generator "pause" saat yield, dan "resume" saat dipanggil lagi.

def hitung_mundur(n):
    print(f"Start hitung mundur dari {n}")
    while n > 0:
        yield n # Pause di sini dan kembalikan n
        n -= 1  # Saat resume, lanjut dari baris ini
    print("Selesai!")

print("\n--- 2. Looping Generator ---")
# Loop `for` otomatis memanggil next() dan menangani StopIteration
for angka in hitung_mundur(3):
    print(f"Angka: {angka}")

# --- 3. Memory Efficiency (List vs Generator) ---
# Generator sangat berguna untuk data besar (Infinite Stream / Large File).

print("\n--- 3. Perbandingan Memori ---")
batas = 1_000_000

# List Comprehension (Disimpan semua di memori)
list_besar = [i * 2 for i in range(batas)]
print(f"Ukuran List: {sys.getsizeof(list_besar)} bytes")

# Generator Expression (Dihitung saat diminta saja)
# Syntax mirip list comprehension tapi pakai kurung ()
gen_besar = (i * 2 for i in range(batas))
print(f"Ukuran Generator: {sys.getsizeof(gen_besar)} bytes (Jauh lebih kecil!)")

# --- 4. Yield From (Delegasi ke Generator Lain) ---
# Fitur Python 3.3+ untuk memanggil generator di dalam generator.

def sub_generator():
    yield "A"
    yield "B"

def main_generator():
    yield "Start"
    yield from sub_generator() # Mengambil semua value dari sub_generator
    yield "End"

print("\n--- 4. Yield From ---")
for item in main_generator():
    print(item)