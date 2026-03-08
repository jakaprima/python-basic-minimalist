# TUTORIAL: 77 Unveiling Insights Through Summary Statistics & Data Transformation
# Exploratory Data Analysis (EDA) dimulai dengan memahami karakteristik dasar data.
# Kita akan menggunakan method seperti .describe(), .info(), .value_counts(), dan transformasi data.

import pandas as pd
import numpy as np

# --- Setup Data Dummy ---
np.random.seed(42)
data = {
    'Produk': np.random.choice(['Laptop', 'Mouse', 'Monitor', 'Keyboard'], 100),
    'Harga': np.random.randint(100000, 5000000, 100),
    'Terjual': np.random.randint(1, 50, 100),
    'Cabang': np.random.choice(['Jakarta', 'Bandung', 'Surabaya'], 100),
    'Tanggal': pd.date_range(start='2023-01-01', periods=100)
}
df = pd.DataFrame(data)

# Menambahkan beberapa nilai NaN untuk demo
df.loc[0:5, 'Harga'] = np.nan

print("--- Preview Data ---")
print(df.head())

# --- 1. Summary Statistics (Statistik Deskriptif) ---
print("\n--- 1. Summary Statistics ---")

# .info() memberikan gambaran tipe data dan missing values
print("\n[INFO] Struktur Data:")
df.info()

# .describe() memberikan statistik dasar (count, mean, std, min, max, quartiles)
# Secara default hanya untuk kolom numerik.
print("\n[DESCRIBE] Statistik Numerik:")
print(df.describe())

# .describe(include='object') untuk kolom kategorikal
print("\n[DESCRIBE] Statistik Kategorikal:")
print(df.describe(include='object'))

# .value_counts() untuk menghitung frekuensi data unik
print("\n[VALUE COUNTS] Frekuensi Produk:")
print(df['Produk'].value_counts())


# --- 2. Data Transformation (Transformasi Data) ---
print("\n--- 2. Data Transformation ---")

# a. Handling Missing Values
# Mengisi NaN di kolom 'Harga' dengan rata-rata harga
mean_harga = df['Harga'].mean()
df['Harga'] = df['Harga'].fillna(mean_harga)
print(f"Missing values di 'Harga' setelah diisi rata-rata: {df['Harga'].isna().sum()}")

# b. Feature Engineering (Membuat Kolom Baru)
# Misal: Total Pendapatan = Harga * Terjual
df['Total_Pendapatan'] = df['Harga'] * df['Terjual']
print("\n[TRANSFORM] Kolom 'Total_Pendapatan' ditambahkan:")
print(df[['Produk', 'Harga', 'Terjual', 'Total_Pendapatan']].head())

# c. Binning (Pengelompokan Numerik ke Kategorikal)
# Mengelompokkan harga menjadi 'Murah', 'Sedang', 'Mahal'
# pd.cut() membagi berdasarkan nilai (value range)
# pd.qcut() membagi berdasarkan kuantitas (jumlah data sama per bin)

labels = ['Murah', 'Sedang', 'Mahal']
df['Kategori_Harga'] = pd.qcut(df['Harga'], q=3, labels=labels)

print("\n[BINNING] Kategori Harga (qcut):")
print(df[['Harga', 'Kategori_Harga']].head(10))
print("\nDistribusi Kategori Harga:")
print(df['Kategori_Harga'].value_counts())