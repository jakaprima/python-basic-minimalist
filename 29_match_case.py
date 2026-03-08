# TUTORIAL: Structural Pattern Matching (Match Case)
# Fitur ini baru ada di Python 3.10+.
# Ini adalah versi "Switch Case" yang sangat powerful di Python.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(f"Status 404: {http_error(404)}")
print(f"Status 500: {http_error(500)}")

# --- Pattern Matching dengan Struktur Data ---
# Match case bisa mengecek isi list/dictionary secara mendalam.

def proses_command(command):
    match command:
        case ["quit"]:
            print("Keluar dari program...")
        case ["load", filename]:
            print(f"Meload file: {filename}")
        case ["save", filename]:
            print(f"Menyimpan ke: {filename}")
        case ["user", name, "admin"]:
            print(f"User {name} adalah admin.")
        case ["user", name, role]:
            print(f"User {name} memiliki role {role}.")
        case _:
            print("Perintah tidak dikenali.")

# Contoh penggunaan
proses_command(["load", "data.txt"])
proses_command(["user", "Jaka", "admin"])
proses_command(["user", "Budi", "guest"])
proses_command(["hapus", "semua"]) # Masuk ke case _

# Kelebihan dibanding If-Else:
# 1. Lebih bersih (clean code).
# 2. Bisa langsung unpack variable (seperti `filename` di atas).
# 3. Bisa mengecek struktur data kompleks.