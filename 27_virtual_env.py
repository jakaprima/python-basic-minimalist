# TUTORIAL: Virtual Environment (venv) dan requirements.txt
# INI ADALAH MATERI KONSEP, BUKAN KODE UNTUK DIJALANKAN LANGSUNG.

# MASALAH:
# Jika Anda mengerjakan 2 project (Project A dan Project B).
# Project A butuh library `requests` versi 2.20.
# Project B butuh library `requests` versi 2.28.
# Jika Anda install global, salah satu project pasti akan error karena versinya tidak cocok.

# SOLUSI: Virtual Environment (venv)
# `venv` membuat folder terisolasi untuk setiap project, yang berisi interpreter Python
# dan library-library yang spesifik untuk project tersebut.

# --- CARA PENGGUNAAN (di Terminal/CMD) ---

# 1. Masuk ke folder project Anda:
# cd /path/to/your/project

# 2. Buat Virtual Environment:
# Perintah ini akan membuat folder bernama 'venv' di dalam direktori project Anda.
# python -m venv venv

# 3. Aktifkan Virtual Environment:
# (Windows)
# venv\Scripts\activate

# (Mac/Linux)
# source venv/bin/activate

# Setelah aktif, nama (venv) akan muncul di awal baris terminal Anda.
# Sekarang, `pip install` hanya akan memasang library di dalam folder `venv` ini.

# 4. Install library yang dibutuhkan:
# (venv) pip install requests

# 5. Membuat file `requirements.txt`:
# File ini berfungsi untuk mendaftar semua library yang dibutuhkan project Anda.
# (venv) pip freeze > requirements.txt

# 6. Jika orang lain ingin menjalankan project Anda:
# Mereka cukup membuat venv, mengaktifkannya, lalu menjalankan:
# (venv) pip install -r requirements.txt
# Ini akan otomatis menginstall semua library yang ada di file requirements.txt.