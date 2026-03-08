# TUTORIAL: Membaca dan Menulis File CSV
# CSV (Comma Separated Values) adalah format data tabular yang sangat umum.
# Python punya module bawaan `csv` untuk menanganinya dengan mudah.

import csv
import os

# Data contoh (List of Lists)
data_siswa = [
    ["Nama", "Kelas", "Nilai"],
    ["Jaka", "12A", 90],
    ["Budi", "12B", 85],
    ["Citra", "12A", 95]
]

filename = "data_siswa.csv"

# --- 1. Menulis CSV (Writer) ---
# `newline=''` penting di Windows agar tidak ada baris kosong ganda.

print("--- 1. Menulis CSV ---")
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Menulis banyak baris sekaligus
    writer.writerows(data_siswa)
    
    # Menulis satu baris tambahan
    writer.writerow(["Dodi", "12C", 80])

print(f"File {filename} berhasil dibuat.")


# --- 2. Membaca CSV (Reader) ---
# Membaca file baris per baris sebagai list.

print("\n--- 2. Membaca CSV (sebagai List) ---")
with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 
        # row adalah list, misal: ['Jaka', '12A', '90']


# --- 3. Menulis CSV dengan Dictionary (DictWriter) ---
# Lebih aman karena kita memetakan data berdasarkan nama kolom (header).

data_dict = [
    {"Nama": "Eka", "Kelas": "11A", "Nilai": 88},
    {"Nama": "Fani", "Kelas": "11B", "Nilai": 92}
]

filename_dict = "data_siswa_dict.csv"
fieldnames = ["Nama", "Kelas", "Nilai"]

print("\n--- 3. Menulis CSV dengan Dictionary ---")
with open(filename_dict, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader() # Menulis baris judul kolom
    writer.writerows(data_dict)

print(f"File {filename_dict} berhasil dibuat.")


# --- 4. Membaca CSV dengan Dictionary (DictReader) ---
# Sangat berguna karena kita bisa akses data pakai key, bukan index angka.

print("\n--- 4. Membaca CSV dengan Dictionary ---")
with open(filename_dict, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # row adalah dict, misal: {'Nama': 'Eka', 'Kelas': '11A', 'Nilai': '88'}
        print(f"{row['Nama']} dari kelas {row['Kelas']} mendapat nilai {row['Nilai']}")