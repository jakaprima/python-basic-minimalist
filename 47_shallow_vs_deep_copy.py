# TUTORIAL: Shallow Copy vs Deep Copy
# Memahami bagaimana Python menyalin objek sangat penting untuk menghindari bug
# saat bekerja dengan data mutable (seperti list di dalam list).

import copy

# --- 1. Assignment (Bukan Copy) ---
# Tanda sama dengan (=) tidak membuat salinan baru.
# Ia hanya memberikan "nama lain" (reference) ke objek yang sama.

list_asli = [1, 2, [3, 4]]
list_assign = list_asli

print("--- 1. Assignment (=) ---")
print(f"Asli: {list_asli}")
print(f"Assign: {list_assign}")

# Ubah data di list_assign
list_assign[0] = 99
print(f"Setelah ubah assign[0]:")
print(f"Asli: {list_asli} (Ikut berubah!)")
print(f"Assign: {list_assign}")
print("Kesimpulan: Keduanya menunjuk ke objek memori yang SAMA.\n")


# --- 2. Shallow Copy (Copy Dangkal) ---
# Membuat objek baru, tapi isinya masih referensi ke objek lama.
# Aman untuk data flat (list of integers), tapi TIDAK aman untuk nested objects (list of lists).

list_asli = [1, 2, [3, 4]]
list_shallow = copy.copy(list_asli) # Atau bisa pakai list_asli[:] atau list(list_asli)

print("--- 2. Shallow Copy ---")
# Ubah level pertama (aman)
list_shallow[0] = 100
print(f"Ubah level 1 -> Asli: {list_asli[0]}, Shallow: {list_shallow[0]} (Aman, beda)")

# Ubah nested object (level 2) - BAHAYA
list_shallow[2][0] = 500
print(f"Ubah level 2 -> Asli: {list_asli[2]}, Shallow: {list_shallow[2]} (Ikut berubah!)")
print("Kesimpulan: Shallow copy hanya menyalin 'kulit' luarnya saja.\n")


# --- 3. Deep Copy (Copy Dalam) ---
# Membuat objek baru DAN menyalin semua isinya secara rekursif.
# Benar-benar terpisah dari objek asli.

list_asli = [1, 2, [3, 4]]
list_deep = copy.deepcopy(list_asli)

print("--- 3. Deep Copy ---")
# Ubah level pertama
list_deep[0] = 100
# Ubah nested object
list_deep[2][0] = 500

print(f"Asli: {list_asli}")
print(f"Deep: {list_deep}")
print("Kesimpulan: Deep copy sepenuhnya independen. Perubahan tidak berdampak ke asli.")