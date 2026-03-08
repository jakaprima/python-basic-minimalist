# TUTORIAL: Module `sys` dan Command Line Arguments
# Module `sys` menyediakan akses ke variabel dan fungsi yang berhubungan dengan interpreter Python.
# Salah satu yang paling berguna adalah `sys.argv` untuk membaca argumen dari terminal.

import sys

# --- 1. sys.argv: The List of Arguments ---
# `sys.argv` adalah sebuah list yang berisi argumen command-line.
# - sys.argv[0] selalu nama script itu sendiri.
# - sys.argv[1] adalah argumen pertama, dst.

print("--- 1. Melihat isi sys.argv ---")
print(f"Nama script: {sys.argv[0]}")
print(f"Isi list sys.argv: {sys.argv}")
print(f"Jumlah argumen (termasuk nama script): {len(sys.argv)}")


# --- 2. Mengakses Argumen ---
# Cara ini lebih manual dibanding `argparse`, tapi berguna untuk script sederhana.

print("\n--- 2. Memproses Argumen ---")
# Cek apakah ada argumen yang diberikan selain nama script
if len(sys.argv) > 1:
    # Argumen pertama setelah nama file
    argumen1 = sys.argv[1]
    print(f"Argumen pertama adalah: {argumen1}")
    
    # Looping semua argumen yang diberikan user
    print("Semua argumen dari user:")
    for arg in sys.argv[1:]: # Mulai dari index 1 (slicing)
        print(f"- {arg}")
else:
    print("Tidak ada argumen yang diberikan.")
    print("Coba jalankan dari terminal dengan perintah:")
    print("python 53_sys_argv.py arg1 arg2 'argumen dengan spasi'")


# --- 3. Penggunaan Umum: sys.exit() ---
# `sys.exit()` digunakan untuk menghentikan program, seringkali dengan status code.
# Status 0 = sukses, status > 0 = error.

print("\n--- 3. Contoh dengan sys.exit() ---")
if len(sys.argv) < 3:
    # `file=sys.stderr` adalah best practice untuk pesan error
    print("Error: Script ini butuh setidaknya 2 argumen.", file=sys.stderr) 
    sys.exit(1) # Keluar dari program dengan status error

print("Pesan ini tidak akan muncul jika argumen kurang dari 2.")

# Perbandingan dengan argparse:
# - sys.argv: Manual, cepat untuk script simpel, tidak ada help message otomatis.
# - argparse: Lebih powerful, otomatis generate help, handle tipe data, flag, dll.