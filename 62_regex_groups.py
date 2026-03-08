# TUTORIAL: Regular Expressions Lanjutan (Groups)
# "Groups" adalah bagian dari pola regex yang diapit oleh tanda kurung `()`.
# Mereka sangat berguna untuk mengekstrak bagian-bagian spesifik dari string yang cocok.

import re

log_entry = "ERROR: Transaksi gagal untuk user 'jaka' dari IP 192.168.1.10"

# --- 1. Tanpa Groups: Hanya mengecek apakah pola cocok ---
print("--- 1. Tanpa Groups ---")
match = re.search("user '.*' from IP .*", log_entry)
if match:
    print(f"Pola cocok: {match.group(0)}") # group(0) adalah keseluruhan string yang cocok

# --- 2. Dengan Numbered Groups: Mengekstrak data ---
# Pola: user '(.*)' from IP (.*)
# Group 1: (.*) -> akan menangkap username
# Group 2: (.*) -> akan menangkap alamat IP

print("\n--- 2. Numbered Groups ---")
match = re.search("user '(.*)' from IP (.*)", log_entry)
if match:
    # .groups() mengembalikan tuple dari semua grup yang ditangkap
    print(f"Semua grup: {match.groups()}") # ('jaka', '192.168.1.10')
    
    # Mengakses grup berdasarkan nomor indeks (mulai dari 1)
    username = match.group(1)
    ip_address = match.group(2)
    print(f"Username: {username}")
    print(f"Alamat IP: {ip_address}")

# --- 3. Dengan Named Groups: Kode lebih mudah dibaca ---
# Pola: (?P<nama_grup>...)
# Ini jauh lebih baik untuk pola yang kompleks karena tidak bergantung pada urutan.

print("\n--- 3. Named Groups ---")
pattern = re.compile(r"user '(?P<user>.*)' from IP (?P<ip>[\d.]+)")
match = pattern.search(log_entry)

if match:
    # .groupdict() mengembalikan dictionary dari semua named group
    print(f"Grup sebagai dict: {match.groupdict()}")
    
    # Mengakses grup berdasarkan nama
    username = match.group("user")
    ip_address = match.group("ip")
    print(f"Username: {username}")
    print(f"Alamat IP: {ip_address}")

# --- 4. `findall` dengan Groups ---
# Perilaku `findall` berubah jika ada grup.
# - Tanpa grup: Mengembalikan list of strings (semua match).
# - Dengan grup: Mengembalikan list of tuples (setiap tuple berisi string dari grup).

text = "Email saya jaka@mail.com dan budi@mail.com"
print("\n--- 4. `findall` dengan Groups ---")

# Tanpa grup
emails_full = re.findall(r"[\w.]+@[\w.]+", text)
print(f"findall tanpa grup: {emails_full}")

# Dengan grup (hanya menangkap bagian sebelum dan sesudah @)
emails_parts = re.findall(r"([\w.]+)@([\w.]+)", text)
print(f"findall dengan grup: {emails_parts}")