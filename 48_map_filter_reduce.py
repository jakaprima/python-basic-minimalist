# TUTORIAL: Map, Filter, dan Reduce
# Tiga fungsi ini adalah fondasi dari "Functional Programming" di Python.
# Mereka memungkinkan kita memproses data iterable (list, tuple, dll) tanpa loop `for` eksplisit.

from functools import reduce

# Data contoh
angka = [1, 2, 3, 4, 5]

# --- 1. map(function, iterable) ---
# Mengaplikasikan fungsi ke SETIAP item dalam iterable.
# Mengembalikan iterator (perlu di-cast ke list/tuple untuk melihat hasilnya).

def kuadrat(n):
    return n * n

# Cara Biasa (Loop)
hasil_loop = []
for n in angka:
    hasil_loop.append(kuadrat(n))

# Cara Map
# map(kuadrat, angka) -> mengembalikan map object
hasil_map = list(map(kuadrat, angka))

print("--- 1. Map ---")
print(f"Data Asli: {angka}")
print(f"Hasil Map (Kuadrat): {hasil_map}")

# Menggunakan Lambda dengan Map (Lebih ringkas)
hasil_map_lambda = list(map(lambda x: x * 2, angka))
print(f"Hasil Map (Kali 2): {hasil_map_lambda}")


# --- 2. filter(function, iterable) ---
# Menyaring item dalam iterable.
# Hanya item yang membuat fungsi bernilai True yang akan disimpan.

def cek_genap(n):
    return n % 2 == 0

# Cara Filter
hasil_filter = list(filter(cek_genap, angka))

print("\n--- 2. Filter ---")
print(f"Hasil Filter (Genap): {hasil_filter}")

# Menggunakan Lambda dengan Filter
hasil_filter_lambda = list(filter(lambda x: x > 3, angka))
print(f"Hasil Filter (Lebih dari 3): {hasil_filter_lambda}")


# --- 3. reduce(function, iterable) ---
# Melakukan komputasi kumulatif pada list.
# Contoh: ((((1+2)+3)+4)+5)
# Note: reduce tidak ada di global namespace Python 3, harus import dari functools.

def jumlahkan(x, y):
    return x + y

# Cara Reduce
# Langkah: 1+2=3 -> 3+3=6 -> 6+4=10 -> 10+5=15
hasil_reduce = reduce(jumlahkan, angka)

print("\n--- 3. Reduce ---")
print(f"Hasil Reduce (Penjumlahan): {hasil_reduce}")

# Menggunakan Lambda dengan Reduce (Perkalian)
hasil_reduce_lambda = reduce(lambda x, y: x * y, angka)
print(f"Hasil Reduce (Perkalian): {hasil_reduce_lambda}")


# --- 4. Alternatif Modern: List Comprehension ---
# Di Python modern, List Comprehension seringkali lebih disukai karena lebih mudah dibaca.

print("\n--- 4. Perbandingan dengan List Comprehension ---")
print(f"Map vs List Comp: {list(map(lambda x: x**2, angka)) == [x**2 for x in angka]}")
print(f"Filter vs List Comp: {list(filter(lambda x: x%2==0, angka)) == [x for x in angka if x%2==0]}")