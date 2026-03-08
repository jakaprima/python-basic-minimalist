# TUTORIAL: 74 Mastering Data Visualization (Basics, Bar Charts, Histograms)
# Matplotlib adalah library dasar untuk plotting di Python.
# Seaborn dibangun di atas Matplotlib, memberikan tampilan lebih bagus dan syntax lebih simpel.

# Prasyarat: pip install matplotlib seaborn pandas

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- Setup Data Dummy ---
data = {
    'Kategori': ['Elektronik', 'Pakaian', 'Makanan', 'Elektronik', 'Pakaian', 'Makanan', 'Elektronik'],
    'Penjualan': [500, 300, 150, 600, 350, 200, 550],
    'Profit': [50, 30, 15, 60, 35, 20, 55],
    'Rating': [4.5, 4.0, 3.5, 4.8, 4.2, 3.8, 4.6]
}
df = pd.DataFrame(data)

# Set style Seaborn agar lebih cantik
sns.set_theme(style="whitegrid")

print("--- Data Preview ---")
print(df.head())

# --- 1. Bar Chart (Visualisasi Data Kategorikal) ---
# Cocok untuk membandingkan jumlah/nilai antar kategori.

plt.figure(figsize=(10, 5)) # Mengatur ukuran gambar (lebar, tinggi)

# Menggunakan Seaborn untuk Bar Chart
# ci=None menghilangkan error bar (garis hitam kecil di atas bar)
sns.barplot(x='Kategori', y='Penjualan', data=df, estimator=sum, errorbar=None, palette='viridis')

plt.title('Total Penjualan per Kategori')
plt.xlabel('Kategori Produk')
plt.ylabel('Total Penjualan')

# Menampilkan plot
# plt.show() # Uncomment baris ini jika menjalankan di local machine/Jupyter
print("\n[INFO] Bar Chart telah dibuat (plt.show() dipanggil).")


# --- 2. Histogram (Visualisasi Distribusi Data) ---
# Cocok untuk melihat sebaran data numerik (misal: sebaran umur, gaji, rating).

# Kita buat data random yang lebih banyak untuk histogram
np.random.seed(42)
data_umur = np.random.normal(loc=30, scale=5, size=1000) # Rata-rata 30, standar deviasi 5

plt.figure(figsize=(10, 5))

# kde=True menambahkan garis kurva estimasi densitas (Kernel Density Estimate)
sns.histplot(data_umur, bins=30, kde=True, color='skyblue')

plt.title('Distribusi Umur Pelanggan')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')

# plt.show()
print("[INFO] Histogram telah dibuat.")


# --- 3. Matplotlib Murni (Contoh Sederhana) ---
# Kadang kita hanya butuh plot cepat tanpa Seaborn.

kategori_unik = df['Kategori'].unique()
total_penjualan = df.groupby('Kategori')['Penjualan'].sum()

plt.figure(figsize=(8, 4))
plt.bar(total_penjualan.index, total_penjualan.values, color='orange')
plt.title('Total Penjualan (Matplotlib)')
plt.xlabel('Kategori')
plt.ylabel('Penjualan')

# plt.show()
print("[INFO] Matplotlib Bar Chart telah dibuat.")