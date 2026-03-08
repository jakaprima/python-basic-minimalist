# TUTORIAL: Module `math` untuk Operasi Matematika
# Module `math` menyediakan akses ke fungsi dan konstanta matematika
# yang didefinisikan oleh standar C.

import math

# --- 1. Konstanta Matematika ---
print("--- 1. Konstanta ---")
print(f"Nilai Pi (π): {math.pi}")
print(f"Nilai Euler (e): {math.e}")


# --- 2. Fungsi Pangkat dan Logaritma ---
print("\n--- 2. Pangkat dan Logaritma ---")

# a. Akar kuadrat (Square Root)
print(f"Akar kuadrat dari 81 adalah: {math.sqrt(81)}")

# b. Pangkat (Power)
# math.pow(x, y) sama dengan x ** y, tapi mengembalikan float.
print(f"3 pangkat 4 adalah: {math.pow(3, 4)}")

# c. Logaritma
# Logaritma basis 10 dari 100
print(f"log10(100) adalah: {math.log10(100)}")
# Logaritma basis 2 dari 8
print(f"log2(8) adalah: {math.log2(8)}")


# --- 3. Fungsi Trigonometri ---
# Fungsi trigonometri di Python bekerja dengan RADIAN, bukan derajat.
print("\n--- 3. Trigonometri ---")

# Konversi 90 derajat ke radian
sudut_radian = math.radians(90)
print(f"90 derajat = {sudut_radian:.4f} radian")

# Menghitung sinus dari 90 derajat
# Hasilnya mungkin tidak persis 1.0 karena keterbatasan floating point
print(f"Sinus 90 derajat adalah: {math.sin(sudut_radian)}")


# --- 4. Pembulatan (Rounding) ---
print("\n--- 4. Pembulatan ---")
angka = 4.7
print(f"Angka asli: {angka}")
print(f"math.ceil() (bulatkan ke atas): {math.ceil(angka)}")   # Hasil: 5
print(f"math.floor() (bulatkan ke bawah): {math.floor(angka)}") # Hasil: 4


# --- 5. Faktorial ---
print("\n--- 5. Faktorial ---")
# Faktorial 5! = 5 * 4 * 3 * 2 * 1
print(f"Faktorial dari 5 adalah: {math.factorial(5)}")