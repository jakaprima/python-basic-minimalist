# TUTORIAL: Command Line Arguments (argparse)
# Mengambil input dari terminal saat menjalankan script.
# Contoh cara jalanin: python 31_argparse.py --nama Jaka --umur 25

import argparse

# 1. Buat parser
parser = argparse.ArgumentParser(description="Program sapaan sederhana.")

# 2. Tambahkan argumen yang diharapkan
parser.add_argument("--nama", type=str, help="Nama user", required=True)
parser.add_argument("--umur", type=int, help="Umur user", default=0)
parser.add_argument("--verbose", action="store_true", help="Tampilkan log detail")

# 3. Parse argumen (Hanya berjalan jika dijalankan lewat terminal)
# Kita bungkus try-except agar tidak error saat dijalankan langsung di editor tanpa argumen
try:
    args = parser.parse_args()
    
    if args.verbose:
        print("--- Mode Verbose Aktif ---")
        print(f"Raw arguments: {args}")

    print(f"Halo, {args.nama}!")
    if args.umur > 0:
        print(f"Wah, kamu berumur {args.umur} tahun.")
        
except SystemExit:
    # argparse akan exit jika argumen wajib tidak diisi
    print("\n[INFO] Jalankan file ini lewat terminal dengan perintah:")
    print("python 31_argparse.py --nama Jaka --umur 25")
    print("atau gunakan: python 31_argparse.py -h (untuk bantuan)")