# TUTORIAL: Itertools untuk Looping Efisien
# Module `itertools` menyediakan fungsi-fungsi iterator yang hemat memori
# untuk menangani skenario looping yang kompleks.

import itertools
import time

# --- 1. Infinite Iterators (Hati-hati, butuh break!) ---

print("--- 1. Count (Infinite Counter) ---")
# count(start=0, step=1)
counter = itertools.count(start=10, step=2)

for i in counter:
    print(i, end=" ")
    if i >= 20:
        break
print("\n")

print("--- 2. Cycle (Infinite Loop over Iterable) ---")
lampu_lalu_lintas = itertools.cycle(["Merah", "Kuning", "Hijau"])

count = 0
for warna in lampu_lalu_lintas:
    print(warna, end=" -> ")
    count += 1
    if count >= 6:
        break
print("STOP\n")


# --- 2. Combinatoric Iterators (Kombinasi & Permutasi) ---

huruf = ['A', 'B', 'C']

print("--- 3. Permutations (Urutan Penting) ---")
# Semua kemungkinan urutan 2 huruf dari ['A', 'B', 'C']
# (A, B) beda dengan (B, A)
perms = list(itertools.permutations(huruf, 2))
print(f"Permutasi 2 huruf: {perms}")

print("\n--- 4. Combinations (Urutan Tidak Penting) ---")
# Semua kemungkinan grup 2 huruf
# (A, B) sama dengan (B, A), jadi hanya diambil satu
combs = list(itertools.combinations(huruf, 2))
print(f"Kombinasi 2 huruf: {combs}")

print("\n--- 5. Product (Cartesian Product / Nested Loop) ---")
# Sama seperti: for x in warna: for y in ukuran: ...
warna = ['Merah', 'Biru']
ukuran = ['S', 'M']

prod = list(itertools.product(warna, ukuran))
print(f"Product: {prod}")


# --- 3. Terminating Iterators ---

print("\n--- 6. Chain (Menggabungkan Iterable) ---")
# Menggabungkan beberapa list/tuple menjadi satu sequence panjang tanpa membuat list baru di memori.
angka1 = [1, 2, 3]
angka2 = [4, 5, 6]
angka3 = [7, 8, 9]

gabungan = itertools.chain(angka1, angka2, angka3)
print(f"Chain: {list(gabungan)}")

print("\n--- 7. Zip Longest ---")
# zip() biasa akan berhenti di item terpendek.
# zip_longest() akan lanjut sampai item terpanjang habis, mengisi kekosongan dengan `fillvalue`.

nama = ["Ali", "Budi"]
nilai = [80, 90, 100] # Nilai lebih panjang dari nama

zipped = itertools.zip_longest(nama, nilai, fillvalue="-")
print("Zip Longest:")
for n, s in zipped:
    print(f"{n}: {s}")