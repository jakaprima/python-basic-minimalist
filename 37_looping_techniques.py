# TUTORIAL: Teknik Looping Lanjutan (zip, reversed)

# --- 1. zip() ---
# `zip()` digunakan untuk menggabungkan beberapa iterable (list, tuple, dll)
# dan melakukan iterasi secara paralel.

list_nama = ["Jaka", "Budi", "Citra"]
list_nilai = [85, 90, 95]
list_kota = ["Jakarta", "Bandung", "Surabaya"]

print("--- Menggunakan zip() ---")
for nama, nilai, kota in zip(list_nama, list_nilai, list_kota):
    print(f"{nama} dari {kota} mendapat nilai {nilai}.")
# Output:
# Jaka dari Jakarta mendapat nilai 85.
# Budi dari Bandung mendapat nilai 90.
# Citra dari Surabaya mendapat nilai 95.

# Catatan: zip() akan berhenti saat iterable terpendek habis.

# --- 2. reversed() ---
# `reversed()` digunakan untuk melakukan iterasi pada sebuah sequence dari belakang ke depan.

angka = [1, 2, 3, 4, 5]

print("\n--- Menggunakan reversed() ---")
for n in reversed(angka):
    print(n)
# Output:
# 5, 4, 3, 2, 1

# Ini lebih efisien dan lebih mudah dibaca daripada `angka[::-1]`.