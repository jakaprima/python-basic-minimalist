# TUTORIAL: Module `glob` untuk Mencari File dengan Pola
# Module `glob` sangat berguna untuk menemukan file yang cocok dengan pola
# tertentu (wildcard), mirip seperti di terminal.

import glob
import os

# --- Setup: Membuat file dan direktori dummy untuk demo ---
def setup_demo_files():
    print("--- Setup: Membuat file dan direktori dummy ---")
    os.makedirs("glob_test/subdir", exist_ok=True)
    with open("glob_test/a.txt", "w") as f: f.write("a")
    with open("glob_test/b.txt", "w") as f: f.write("b")
    with open("glob_test/data1.py", "w") as f: f.write("py1")
    with open("glob_test/data2.py", "w") as f: f.write("py2")
    with open("glob_test/subdir/c.txt", "w") as f: f.write("c")
    print("Setup selesai.\n")

# --- Cleanup: Menghapus file dan direktori dummy ---
def cleanup_demo_files():
    print("\n--- Cleanup: Menghapus file dan direktori dummy ---")
    os.remove("glob_test/subdir/c.txt")
    os.rmdir("glob_test/subdir")
    os.remove("glob_test/a.txt")
    os.remove("glob_test/b.txt")
    os.remove("glob_test/data1.py")
    os.remove("glob_test/data2.py")
    os.rmdir("glob_test")
    print("Cleanup selesai.")


if __name__ == "__main__":
    setup_demo_files()

    # --- 1. Wildcard `*` (Mencocokkan semua karakter) ---
    print("1. Mencari semua file .txt di direktori 'glob_test':")
    # Pola: 'glob_test/*.txt'
    txt_files = glob.glob("glob_test/*.txt")
    print(txt_files)

    print("\n2. Mencari semua file python yang diawali 'data':")
    # Pola: 'glob_test/data*.py'
    py_files = glob.glob("glob_test/data*.py")
    print(py_files)

    # --- 2. Wildcard `?` (Mencocokkan satu karakter) ---
    print("\n3. Mencari file python dengan nama 'data' diikuti 1 karakter:")
    # Pola: 'glob_test/data?.py'
    py_files_single_char = glob.glob("glob_test/data?.py")
    print(py_files_single_char)

    # --- 3. Pencarian Rekursif dengan `**` ---
    # `**` akan mencari di direktori saat ini dan semua subdirektori.
    # Membutuhkan argumen `recursive=True`.

    print("\n4. Mencari semua file .txt di dalam 'glob_test' dan semua subdirektorinya:")
    # Pola: 'glob_test/**/*.txt'
    all_txt_files = glob.glob("glob_test/**/*.txt", recursive=True)
    print(all_txt_files)

    # Jalankan cleanup setelah selesai
    cleanup_demo_files()