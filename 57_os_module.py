# TUTORIAL: Module `os` untuk Interaksi dengan Sistem Operasi
# Module `os` menyediakan cara untuk menggunakan fungsionalitas yang bergantung
# pada sistem operasi, seperti membaca atau menulis ke filesystem.

import os

# --- 1. Mendapatkan Informasi Dasar ---
print("--- 1. Informasi Dasar ---")

# a. Get Current Working Directory (getcwd)
current_dir = os.getcwd()
print(f"Direktori saat ini: {current_dir}")

# b. List Directory Contents (listdir)
print(f"Isi direktori '{current_dir}':")
print(os.listdir())


# --- 2. Membuat dan Menghapus Direktori ---
print("\n--- 2. Manajemen Direktori ---")

dir_name = "test_dir_os"
try:
    # a. Membuat direktori
    os.mkdir(dir_name)
    print(f"Direktori '{dir_name}' berhasil dibuat.")
except FileExistsError:
    print(f"Direktori '{dir_name}' sudah ada.")


# --- 3. Bekerja dengan Path (os.path) - SANGAT PENTING! ---
print("\n--- 3. Bekerja dengan Path ---")

# a. Menggabungkan path (os.path.join)
# Ini adalah cara paling aman dan portabel untuk membuat path,
# karena otomatis menggunakan separator yang benar ('\' di Windows, '/' di Linux/Mac).
file_name = "catatan.txt"
file_path = os.path.join(dir_name, file_name)
print(f"Path yang aman untuk file: {file_path}")

# b. Mengecek keberadaan path (exists, isfile, isdir)
print(f"Apakah '{dir_name}' ada? {os.path.exists(dir_name)}")
print(f"Apakah '{dir_name}' adalah direktori? {os.path.isdir(dir_name)}")
print(f"Apakah '{file_path}' adalah file? {os.path.isfile(file_path)}")


# --- 4. Manajemen File ---
print("\n--- 4. Manajemen File ---")

# Membuat file kosong di dalam direktori baru
with open(file_path, "w") as f:
    f.write("Halo dari modul OS!")
print(f"File '{file_path}' berhasil dibuat.")

# Mengganti nama file
new_file_path = os.path.join(dir_name, "catatan_baru.txt")
os.rename(file_path, new_file_path)
print(f"File diubah namanya menjadi '{new_file_path}'")


# --- 5. Mengakses Environment Variables ---
print("\n--- 5. Environment Variables ---")
# Mengambil nilai dari environment variable 'PATH' (contoh)
path_env = os.getenv("PATH")
print(f"Isi env 'PATH' (sebagian): {path_env[:50]}...")


# --- Cleanup: Hapus file dan direktori yang dibuat ---
os.remove(new_file_path)
os.rmdir(dir_name)
print(f"\nCleanup: File dan direktori '{dir_name}' telah dihapus.")