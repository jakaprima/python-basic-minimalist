# TUTORIAL: 73 Data Cleaning Essentials with Pandas
# Data di dunia nyata seringkali "kotor": ada duplikat, nilai yang aneh (outlier),
# atau tipe data yang salah. Membersihkan data adalah langkah krusial sebelum analisis.

# Prasyarat: pip install pandas

import pandas as pd
import numpy as np

# --- Membuat DataFrame "kotor" untuk demo ---
data = {
    'id_transaksi': [1, 2, 3, 4, 2, 5, 6, 7],
    'tanggal': ['2023-01-10', '2023-01-11', '2023-01-12', '2023-01-13', '2023-01-11', '2023-01-14', '2023-01-15', '2023-01-16'],
    'jumlah_pembelian': ['150000', '200000', '50000', '250000', '200000', '10000000', '180000', '220000'], # Ada outlier & tipe data string
    'rating': [4.5, 4.0, 5.0, 3.5, 4.0, 4.2, 'N/A', 4.8] # Ada tipe data string 'N/A'
}
df = pd.DataFrame(data)

print("--- Data Awal (Kotor) ---")
print(df)
print("\nInfo Tipe Data Awal:")
df.info()

# --- 1. Menangani Duplikat ---
print("\n--- 1. Menangani Duplikat ---")

# a. Mencari baris duplikat
# keep='first' (default) akan menandai duplikat kedua dan seterusnya sebagai True
duplicate_rows = df[df.duplicated()]
print("Baris duplikat ditemukan:")
print(duplicate_rows)

# b. Menghapus baris duplikat
# inplace=False (default) akan membuat salinan baru, tidak mengubah DataFrame asli.
df_cleaned = df.drop_duplicates()
print("\nDataFrame setelah menghapus duplikat:")
print(df_cleaned)


# --- 2. Mengonversi Tipe Data ---
print("\n--- 2. Mengonversi Tipe Data ---")

# a. Mengonversi 'jumlah_pembelian' ke numerik
# errors='coerce' akan mengubah nilai yang tidak bisa dikonversi menjadi NaN (Not a Number)
df_cleaned['jumlah_pembelian'] = pd.to_numeric(df_cleaned['jumlah_pembelian'], errors='coerce')

# b. Mengonversi 'rating' ke numerik
df_cleaned['rating'] = pd.to_numeric(df_cleaned['rating'], errors='coerce')

# c. Mengonversi 'tanggal' ke datetime
df_cleaned['tanggal'] = pd.to_datetime(df_cleaned['tanggal'], errors='coerce')

print("\nInfo Tipe Data setelah konversi:")
df_cleaned.info()
# Perhatikan 'jumlah_pembelian' dan 'rating' sekarang float64, dan 'tanggal' adalah datetime64

# Kita bisa mengisi nilai NaN jika perlu, misal dengan rata-rata rating
mean_rating = df_cleaned['rating'].mean()
df_cleaned['rating'].fillna(mean_rating, inplace=True)
print("\nDataFrame setelah konversi dan mengisi nilai N/A pada rating:")
print(df_cleaned)


# --- 3. Menangani Outliers (Nilai Ekstrem) ---
# Salah satu cara umum adalah menggunakan metode Interquartile Range (IQR).
# Outlier adalah data yang berada di luar Q1 - 1.5*IQR dan Q3 + 1.5*IQR.
print("\n--- 3. Menangani Outliers pada 'jumlah_pembelian' ---")

Q1 = df_cleaned['jumlah_pembelian'].quantile(0.25)
Q3 = df_cleaned['jumlah_pembelian'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Batas Bawah (Lower Bound): {lower_bound}")
print(f"Batas Atas (Upper Bound): {upper_bound}")

# Menemukan outliers
outliers = df_cleaned[(df_cleaned['jumlah_pembelian'] < lower_bound) | (df_cleaned['jumlah_pembelian'] > upper_bound)]
print("\nOutlier ditemukan:")
print(outliers)

# Membuat DataFrame baru tanpa outliers
df_no_outliers = df_cleaned[(df_cleaned['jumlah_pembelian'] >= lower_bound) & (df_cleaned['jumlah_pembelian'] <= upper_bound)]

print("\nDataFrame Final (Bersih) tanpa outliers:")
print(df_no_outliers)