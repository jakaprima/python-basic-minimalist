# TUTORIAL: 79 Understanding Correlation Analysis
# Korelasi mengukur seberapa kuat hubungan linear antara dua variabel numerik.
# Nilai korelasi berkisar dari -1 hingga 1.
# 1: Korelasi positif sempurna (Satu naik, yang lain naik)
# -1: Korelasi negatif sempurna (Satu naik, yang lain turun)
# 0: Tidak ada korelasi linear

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Setup Data Dummy ---
np.random.seed(42)
n = 100

# Variabel X
jam_belajar = np.random.normal(5, 2, n)

# Variabel Y1 (Korelasi Positif dengan X)
# Nilai ujian naik seiring jam belajar bertambah (+ noise)
nilai_ujian = 50 + (jam_belajar * 8) + np.random.normal(0, 5, n)

# Variabel Y2 (Korelasi Negatif dengan X)
# Waktu main game turun seiring jam belajar bertambah
waktu_game = 10 - (jam_belajar * 0.8) + np.random.normal(0, 1, n)

# Variabel Y3 (Tidak Berkorelasi / Acak)
nomor_sepatu = np.random.normal(40, 2, n)

df = pd.DataFrame({
    'Jam_Belajar': jam_belajar,
    'Nilai_Ujian': nilai_ujian,
    'Waktu_Game': waktu_game,
    'Nomor_Sepatu': nomor_sepatu
})

print("--- Preview Data ---")
print(df.head())

# --- 1. Menghitung Matriks Korelasi ---
print("\n--- 1. Correlation Matrix ---")

# .corr() menghitung korelasi Pearson secara default
correlation_matrix = df.corr()

print(correlation_matrix)

print("\nAnalisis:")
print(f"Korelasi Belajar vs Nilai: {correlation_matrix.loc['Jam_Belajar', 'Nilai_Ujian']:.2f} (Positif Kuat)")
print(f"Korelasi Belajar vs Game: {correlation_matrix.loc['Jam_Belajar', 'Waktu_Game']:.2f} (Negatif Kuat)")
print(f"Korelasi Belajar vs Sepatu: {correlation_matrix.loc['Jam_Belajar', 'Nomor_Sepatu']:.2f} (Lemah/Nol)")


# --- 2. Visualisasi Korelasi (Heatmap) ---
print("\n--- 2. Visualisasi Heatmap ---")

plt.figure(figsize=(8, 6))

# annot=True menampilkan angka korelasi di dalam kotak
# cmap='coolwarm' memberikan warna merah (positif) dan biru (negatif)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)

plt.title('Correlation Heatmap')
# plt.show()
print("[INFO] Heatmap korelasi telah dibuat.")