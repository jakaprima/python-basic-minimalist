# TUTORIAL: HTTP Bearer Token Authentication (Login/Register)
# Ini adalah simulasi alur otentikasi dasar:
# 1. Register: User mendaftar dengan username & password. Password di-hash.
# 2. Login: User login, jika berhasil, server memberikan "Bearer Token".
# 3. Authenticated Request: User menggunakan token tersebut di header `Authorization`
#    untuk mengakses resource yang dilindungi.

import hashlib
import os

# --- Simulasi Database User ---
# Di aplikasi nyata, ini akan menjadi tabel di database (PostgreSQL, dll.)
# Format: {username: hashed_password}
user_database = {}

# --- Simulasi Database Token Aktif ---
# Di aplikasi nyata, ini bisa berupa JWT (JSON Web Token) atau token di database
valid_tokens = set()

# --- 1. Fungsi Registrasi ---
def register_user(username, password):
    """Mendaftarkan user baru dengan menghash password."""
    if username in user_database:
        print(f"❌ Registrasi Gagal: Username '{username}' sudah ada.")
        return False
    
    # Hash password sebelum disimpan (JANGAN PERNAH SIMPAN PLAIN TEXT PASSWORD)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_database[username] = hashed_password
    print(f"✅ Registrasi Berhasil untuk user '{username}'.")
    return True

# --- 2. Fungsi Login ---
def login_user(username, password):
    """Memvalidasi login dan mengembalikan bearer token jika berhasil."""
    if username not in user_database:
        print(f"❌ Login Gagal: User '{username}' tidak ditemukan.")
        return None
        
    # Hash password yang diinput dan bandingkan dengan yang ada di database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user_database[username] == hashed_password:
        # Buat token sederhana untuk demo
        token = f"secret_token_for_{username}_{os.urandom(8).hex()}"
        valid_tokens.add(token)
        print(f"✅ Login Berhasil! Token Anda: {token}")
        return token
    else:
        print("❌ Login Gagal: Password salah.")
        return None

# --- 3. Fungsi yang Membutuhkan Otentikasi ---
def get_protected_data(headers):
    """
    Simulasi endpoint API yang dilindungi.
    Membutuhkan header 'Authorization: Bearer <token>'.
    """
    print("\n--- Mencoba akses resource terproteksi ---")
    auth_header = headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Bearer "):
        return {"error": "Header 'Authorization' dengan format 'Bearer <token>' tidak ditemukan."}, 401
        
    token = auth_header.split(" ")[1]
    if token in valid_tokens:
        print("Otentikasi berhasil!")
        return {"data": "Ini adalah data rahasia untuk user yang terotentikasi."}, 200
    else:
        print("Otentikasi gagal! Token tidak valid.")
        return {"error": "Token tidak valid atau sudah kedaluwarsa."}, 403

# --- Demo Alur Lengkap ---
if __name__ == "__main__":
    # Langkah 1: Registrasi
    print("--- Langkah 1: Registrasi ---")
    register_user("jaka", "password123")
    register_user("budi", "passwordku")
    
    # Langkah 2: Login
    print("\n--- Langkah 2: Login ---")
    jaka_token = login_user("jaka", "password123")
    login_user("budi", "password_salah") # Coba login dengan password salah
    
    # Langkah 3: Mengakses Resource Terproteksi
    
    # Skenario A: Sukses dengan token yang valid
    request_headers = {"Authorization": f"Bearer {jaka_token}"}
    data, status_code = get_protected_data(request_headers)
    print(f"Response (Status {status_code}): {data}")

    # Skenario B: Gagal karena token salah
    request_headers_salah = {"Authorization": "Bearer token_palsu_12345"}
    data, status_code = get_protected_data(request_headers_salah)
    print(f"Response (Status {status_code}): {data}")