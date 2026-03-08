# TUTORIAL: 78 Exploring Group By and Pivot Tables
# GroupBy dan Pivot Table adalah teknik powerful untuk meringkas (aggregate) data.
# Mirip dengan fitur Pivot Table di Excel atau GROUP BY di SQL.

import pandas as pd
import numpy as np

# --- Setup Data Dummy ---
np.random.seed(10)
data = {
    'Divisi': np.random.choice(['Sales', 'Marketing', 'IT', 'HR'], 50),
    'Level': np.random.choice(['Junior', 'Senior', 'Manager'], 50),
    'Gaji': np.random.randint(5000000, 20000000, 50),
    'Bonus': np.random.randint(1000000, 5000000, 50),
    'Jam_Kerja': np.random.randint(160, 200, 50)
}
df = pd.DataFrame(data)

print("--- Preview Data ---")
print(df.head())

# --- 1. Group By (Pengelompokan Sederhana) ---
print("\n--- 1. Group By ---")

# Mengelompokkan berdasarkan 'Divisi' dan menghitung rata-rata semua kolom numerik
avg_by_divisi = df.groupby('Divisi').mean(numeric_only=True)
print("\nRata-rata per Divisi:")
print(avg_by_divisi)

# Mengelompokkan berdasarkan multiple kolom
# Menghitung rata-rata Gaji per Divisi dan Level
avg_gaji_level = df.groupby(['Divisi', 'Level'])['Gaji'].mean()
print("\nRata-rata Gaji per Divisi & Level:")
print(avg_gaji_level)

# Multiple Aggregations (agg)
# Menghitung rata-rata, min, dan max Gaji per Divisi
agg_gaji = df.groupby('Divisi')['Gaji'].agg(['mean', 'min', 'max'])
print("\nStatistik Gaji Lengkap per Divisi:")
print(agg_gaji)


# --- 2. Pivot Tables (Tabel Silang) ---
print("\n--- 2. Pivot Tables ---")
# Pivot table memungkinkan kita mengubah bentuk data untuk analisis multidimensi.
# Index: Baris, Columns: Kolom, Values: Nilai yang dihitung, Aggfunc: Fungsi (mean, sum, dll)

# Contoh: Baris=Divisi, Kolom=Level, Isi=Rata-rata Gaji
pivot_gaji = pd.pivot_table(
    df, 
    values='Gaji', 
    index='Divisi', 
    columns='Level', 
    aggfunc='mean'
)

print("\nPivot Table (Rata-rata Gaji):")
# Format output agar lebih mudah dibaca (opsional)
pd.options.display.float_format = '{:,.0f}'.format 
print(pivot_gaji)

# Mengisi nilai kosong (jika ada kombinasi Divisi-Level yang tidak ada datanya)
# pivot_gaji = pivot_gaji.fillna(0)

print("\nAnalisis: Kita bisa dengan mudah membandingkan gaji Senior IT vs Senior Sales.")