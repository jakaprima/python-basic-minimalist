# TUTORIAL: Standard Library Lanjutan (statistics & deque)

import statistics
from collections import deque

# --- 1. Module `statistics` ---
# Berguna untuk kalkulasi matematika statistik dasar.

data_nilai = [80, 95, 78, 85, 90, 100, 85, 70, 65, 95, 85]

print("--- Module Statistics ---")
print(f"Data Nilai: {data_nilai}")

# Mean (Rata-rata)
# Jumlah semua nilai dibagi dengan banyaknya nilai.
rata_rata = statistics.mean(data_nilai)
print(f"Mean (Rata-rata): {rata_rata}")

# Median (Nilai Tengah)
# Nilai yang berada di tengah setelah data diurutkan.
nilai_tengah = statistics.median(data_nilai)
print(f"Median (Nilai Tengah): {nilai_tengah}")

# Mode (Nilai yang Paling Sering Muncul)
modus = statistics.mode(data_nilai)
print(f"Mode (Nilai Paling Sering Muncul): {modus}")


# --- 2. `collections.deque` (Double-Ended Queue) ---
# deque (dibaca "deck") adalah list-like object yang sangat efisien untuk
# menambah (append) dan menghapus (pop) elemen dari kedua ujung (kiri/kanan).
# Sangat ideal untuk implementasi antrian (queue) dan tumpukan (stack).

print("\n--- collections.deque sebagai Antrian (FIFO) ---")

# FIFO: First-In, First-Out (Yang pertama masuk, yang pertama keluar)
antrian_kasir = deque(["Pelanggan 1", "Pelanggan 2", "Pelanggan 3"])
print(f"Antrian awal: {antrian_kasir}")

# Pelanggan baru datang dan masuk ke antrian dari kanan (belakang)
antrian_kasir.append("Pelanggan 4")
print(f"Setelah Pelanggan 4 datang: {antrian_kasir}")

# Kasir melayani pelanggan dari kiri (depan)
pelanggan_dilayani = antrian_kasir.popleft()
print(f"Melayani: {pelanggan_dilayani}")
print(f"Antrian sekarang: {antrian_kasir}")

# Tips: Menggunakan list.pop(0) untuk antrian sangat tidak efisien karena semua elemen lain harus digeser.
# Gunakan deque untuk performa yang jauh lebih baik pada kasus seperti ini.