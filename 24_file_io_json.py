# TUTORIAL: File Input/Output dan JSON
# Menggunakan 'with' statement (Context Manager) adalah cara paling aman membuka file.

import json
import os

# 1. MENULIS FILE TEXT BIASA
pesan = ["Halo ini baris 1", "Ini baris 2", "Coding Python itu seru"]

# 'w' = write (menimpa), 'a' = append (menambah), 'r' = read (membaca)
with open("catatan.txt", "w") as file:
    for baris in pesan:
        file.write(baris + "\n")
print("File catatan.txt berhasil dibuat.")

# 2. MEMBACA FILE TEXT
print("\n--- Membaca File ---")
if os.path.exists("catatan.txt"):
    with open("catatan.txt", "r") as file:
        konten = file.read()
        print(konten)

# 3. JSON (JavaScript Object Notation)
# Format standar untuk API dan config file.

data_user = {
    "nama": "Jaka",
    "umur": 25,
    "hobi": ["Coding", "Gaming"],
    "is_active": True
}

# Menyimpan dictionary ke file JSON (Serialization)
with open("data_user.json", "w") as json_file:
    json.dump(data_user, json_file, indent=4)
print("File data_user.json berhasil dibuat.")

# Membaca file JSON kembali ke Dictionary (Deserialization)
print("\n--- Membaca JSON ---")
with open("data_user.json", "r") as json_file:
    data_loaded = json.load(json_file)
    print(f"Nama: {data_loaded['nama']}")
    print(f"Hobi pertama: {data_loaded['hobi'][0]}")
    print(f"Tipe data loaded: {type(data_loaded)}")

# Tips Project:
# Selalu gunakan module 'json' bawaan python daripada memparsing string manual.
# Gunakan 'indent=4' saat dump agar file json mudah dibaca manusia.