# TUTORIAL: Module `pathlib` (Modern Path Handling)
# `pathlib` adalah cara modern dan object-oriented untuk bekerja dengan path filesystem.
# Ini adalah alternatif yang lebih bersih dan intuitif dibanding `os.path`.

from pathlib import Path
import os

# --- 1. Perbandingan: os.path (string-based) vs pathlib (object-based) ---
# Cara lama (os.path)
old_path = os.path.join(os.getcwd(), "test_dir", "file.txt")

# Cara modern (pathlib)
# Path adalah object, bukan sekadar string.
# Kita bisa menggunakan operator '/' untuk menggabungkan path.
modern_path = Path.cwd() / "test_dir" / "file.txt"

print("--- 1. Perbandingan Path ---")
print(f"os.path: {old_path}")
print(f"pathlib: {modern_path}")
print(f"Tipe object pathlib: {type(modern_path)}\n")


# --- 2. Setup Direktori untuk Demo ---
demo_dir = Path("pathlib_demo")
demo_dir.mkdir(exist_ok=True) # Sama seperti os.mkdir, exist_ok=True mencegah error jika sudah ada


# --- 3. Atribut dan Method Berguna ---
file_path = demo_dir / "laporan.txt"

print("--- 2. Atribut Path ---")
print(f"Path lengkap: {file_path}")
print(f"Parent directory: {file_path.parent}") # Mengambil direktori induk
print(f"Nama file: {file_path.name}")          # Mengambil nama file dengan ekstensi
print(f"Nama file (stem): {file_path.stem}")   # Nama file tanpa ekstensi
print(f"Ekstensi file: {file_path.suffix}")    # Ekstensi file


# --- 4. Interaksi dengan File dan Direktori ---
print("\n--- 3. Interaksi Filesystem ---")

# a. Membuat file kosong (.touch())
file_path.touch()
print(f"File '{file_path}' dibuat dengan .touch()")

# b. Mengecek keberadaan (.exists(), .is_file(), .is_dir())
print(f"Apakah '{file_path}' ada? {file_path.exists()}")
print(f"Apakah '{file_path}' file? {file_path.is_file()}")
print(f"Apakah '{demo_dir}' direktori? {demo_dir.is_dir()}")

# c. Menulis dan Membaca file (lebih simpel!)
file_path.write_text("Halo dari pathlib!")
print(f"Isi file: '{file_path.read_text()}'")

# d. Mengganti nama file (.rename())
new_path = demo_dir / "laporan_final.txt"
file_path.rename(new_path)
print(f"File diubah namanya menjadi: {new_path}")


# --- 5. Mencari File dengan .glob() ---
# .glob() pada Path object mengembalikan generator, lebih efisien.
(demo_dir / "a.log").touch()
(demo_dir / "b.log").touch()

print("\n--- 4. Mencari file dengan .glob() ---")
log_files = list(demo_dir.glob("*.log"))
print(f"Menemukan file log: {log_files}")


# --- Cleanup ---
print("\n--- Cleanup ---")
for f in demo_dir.glob("*"):
    f.unlink() # .unlink() untuk menghapus file
print("Semua file di dalam demo dir dihapus.")
demo_dir.rmdir() # .rmdir() untuk menghapus direktori kosong
print(f"Direktori '{demo_dir}' dihapus.")