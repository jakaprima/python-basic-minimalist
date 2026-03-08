# TUTORIAL: 75 Mastering Box Plots and Scatterplots
# Box Plot: Bagus untuk melihat outlier dan statistik lima serangkai (min, Q1, median, Q3, max).
# Scatterplot: Bagus untuk melihat hubungan (korelasi) antara dua variabel numerik.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- Setup Data Dummy ---
np.random.seed(10)
# Membuat data gaji untuk 3 departemen
gaji_it = np.random.normal(15000000, 2000000, 100)
gaji_hr = np.random.normal(10000000, 1500000, 100)
gaji_sales = np.random.normal(12000000, 3000000, 100)

# Menambahkan outlier ekstrem di IT
gaji_it = np.append(gaji_it, [35000000, 40000000]) 

data = {
    'Gaji': np.concatenate([gaji_it, gaji_hr, gaji_sales]),
    'Departemen': ['IT'] * 102 + ['HR'] * 100 + ['Sales'] * 100,
    'Pengalaman_Tahun': np.random.randint(1, 15, 302)
}
# Menambahkan korelasi buatan: Gaji naik seiring pengalaman
data['Gaji'] = data['Gaji'] + (data['Pengalaman_Tahun'] * 500000)

df = pd.DataFrame(data)
sns.set_theme(style="ticks")

# --- 1. Box Plot (Mendeteksi Outlier) ---
print("--- 1. Box Plot ---")

plt.figure(figsize=(10, 6))

# x=Kategori, y=Numerik
sns.boxplot(x='Departemen', y='Gaji', data=df, palette="Set2")

plt.title('Distribusi Gaji per Departemen (dengan Outlier)')
plt.ylabel('Gaji (IDR)')

# plt.show()
print("[INFO] Box Plot telah dibuat. Perhatikan titik-titik di luar 'kumis' (whiskers) adalah outlier.")


# --- 2. Scatterplot (Melihat Hubungan/Korelasi) ---
print("\n--- 2. Scatterplot ---")

plt.figure(figsize=(10, 6))

# hue='Departemen' memberikan warna berbeda untuk setiap departemen
# alpha=0.6 membuat titik sedikit transparan agar terlihat jika menumpuk
sns.scatterplot(x='Pengalaman_Tahun', y='Gaji', data=df, hue='Departemen', style='Departemen', s=100, alpha=0.7)

plt.title('Hubungan Pengalaman Kerja vs Gaji')
plt.xlabel('Pengalaman (Tahun)')
plt.ylabel('Gaji (IDR)')

# Menambahkan garis regresi (trendline) sederhana untuk seluruh data
# scatter=False agar tidak menggambar ulang titik-titik
sns.regplot(x='Pengalaman_Tahun', y='Gaji', data=df, scatter=False, color='black', line_kws={"linewidth": 1})

# plt.show()
print("[INFO] Scatterplot telah dibuat.")
print("Analisis: Terlihat tren positif, semakin lama pengalaman, gaji cenderung naik.")

# Tips:
# Gunakan `sns.pairplot(df)` jika ingin melihat scatterplot antar SEMUA variabel numerik sekaligus.