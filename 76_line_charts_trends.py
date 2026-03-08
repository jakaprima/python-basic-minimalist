# TUTORIAL: 76 Mastering Line Charts (Visualizing Trends Over Time)
# Line Chart adalah pilihan terbaik untuk data Time Series (runtun waktu).
# Kita bisa melihat tren naik, turun, atau pola musiman.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# --- Setup Data Time Series ---
# Membuat rentang tanggal
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Membuat data dummy penjualan dengan tren naik dan sedikit random noise
np.random.seed(42)
trend = np.linspace(0, 100, len(dates)) # Tren naik linear
seasonality = 10 * np.sin(np.linspace(0, 3.14 * 4, len(dates))) # Pola gelombang
noise = np.random.normal(0, 5, len(dates)) # Random noise

penjualan = 50 + trend + seasonality + noise

df = pd.DataFrame({
    'Tanggal': dates,
    'Penjualan': penjualan
})

sns.set_theme(style="darkgrid")

# --- 1. Line Chart Dasar ---
print("--- 1. Line Chart Dasar ---")

plt.figure(figsize=(12, 6))

# Seaborn otomatis menangani format tanggal di sumbu X
sns.lineplot(x='Tanggal', y='Penjualan', data=df, linewidth=2, color='blue')

plt.title('Tren Penjualan Harian (2023)')
plt.xlabel('Tanggal')
plt.ylabel('Penjualan (Unit)')

# plt.show()
print("[INFO] Line Chart Harian telah dibuat.")


# --- 2. Resampling (Agregasi Bulanan) ---
# Data harian seringkali terlalu "berisik" (noisy).
# Kita bisa merata-ratakan data per bulan agar tren lebih jelas.

print("\n--- 2. Line Chart Bulanan (Resampled) ---")

# Set 'Tanggal' sebagai index agar bisa di-resample
df_monthly = df.set_index('Tanggal').resample('M').mean()

plt.figure(figsize=(12, 6))

# Plot data harian (transparan) sebagai background
plt.plot(df['Tanggal'], df['Penjualan'], alpha=0.3, label='Harian', color='gray')

# Plot data bulanan (tebal) sebagai highlight
plt.plot(df_monthly.index, df_monthly['Penjualan'], linewidth=3, marker='o', color='red', label='Rata-rata Bulanan')

plt.title('Tren Penjualan: Harian vs Rata-rata Bulanan')
plt.legend() # Menampilkan label
# plt.show()
print("[INFO] Line Chart Bulanan telah dibuat.")