# TUTORIAL: Social Login (OAuth 2.0) dengan Facebook
# Ini adalah simulasi alur server-side untuk fitur "Login dengan Facebook".
# Alur ini mendelegasikan otentikasi ke Facebook dan hanya menerima hasilnya.

import os
import json

# --- Simulasi Database User ---
# Di aplikasi nyata, ini akan menjadi tabel di database.
# Kita akan menyimpan facebook_id untuk menautkan akun.
user_database = {}
next_user_id = 1

# --- Simulasi API Facebook (yang akan dipanggil oleh server kita) ---

def simulate_exchange_code_for_token(code):
    """Simulasi menukar authorization code dengan access token."""
    print(f"Server: Menukar kode '{code}' dengan access token ke Facebook...")
    if code == "valid_auth_code_from_facebook":
        # Di dunia nyata, ini adalah request HTTP ke API Facebook
        return "fake_facebook_access_token_12345"
    return None

def simulate_get_facebook_profile(access_token):
    """Simulasi mengambil profil user dari Facebook menggunakan access token."""
    print(f"Server: Mengambil profil FB dengan token '{access_token}'...")
    if access_token == "fake_facebook_access_token_12345":
        # Di dunia nyata, ini adalah request HTTP ke Graph API Facebook
        return {
            "id": "fb_user_101",
            "name": "Jaka Zuckerberg",
            "email": "jaka.zuck@example.com"
        }
    return None

# --- Logika di Server Aplikasi Kita ---

def login_or_register_with_facebook(facebook_profile):
    """
    Mencari user berdasarkan facebook_id. Jika tidak ada, buat user baru.
    Kemudian, buat dan kembalikan token sesi untuk aplikasi kita.
    """
    global next_user_id
    facebook_id = facebook_profile.get("id")

    # Cek apakah user dengan facebook_id ini sudah ada di database kita
    user = None
    for u in user_database.values():
        if u.get("facebook_id") == facebook_id:
            user = u
            break
    
    if user:
        # --- Skenario Login ---
        print(f"User ditemukan di database kita (ID: {user['id']}). Logging in...")
    else:
        # --- Skenario Registrasi ---
        print("User tidak ditemukan. Membuat akun baru...")
        user = {
            "id": next_user_id,
            "name": facebook_profile.get("name"),
            "email": facebook_profile.get("email"),
            "facebook_id": facebook_id,
            "source": "facebook"
        }
        user_database[next_user_id] = user
        next_user_id += 1
        print("Akun baru berhasil dibuat.")

    # Buat token sesi untuk aplikasi kita (bukan token Facebook)
    app_session_token = f"app_token_for_user_{user['id']}_{os.urandom(8).hex()}"
    print(f"✅ Login/Registrasi berhasil! Token sesi aplikasi Anda: {app_session_token}")
    return app_session_token

# --- Demo Alur Lengkap (dari perspektif server) ---
if __name__ == "__main__":
    print("--- Alur Login dengan Facebook (Simulasi Server-Side) ---\n")
    
    # 1. User dialihkan kembali ke aplikasi kita dengan `authorization_code`.
    print("Langkah 1: Aplikasi menerima 'authorization_code' dari Facebook.")
    auth_code = "valid_auth_code_from_facebook"
    
    # 2. Server kita menukar kode itu dengan `access_token`.
    print("\nLangkah 2: Server menukar kode dengan Facebook untuk mendapatkan 'access_token'.")
    fb_access_token = simulate_exchange_code_for_token(auth_code)
    
    # 3. Server kita menggunakan `access_token` untuk mengambil profil user.
    print("\nLangkah 3: Server menggunakan 'access_token' untuk mengambil profil user dari Facebook.")
    profile = simulate_get_facebook_profile(fb_access_token)
    
    # 4. Server kita melakukan login atau registrasi.
    print("\nLangkah 4: Server melakukan login atau registrasi berdasarkan profil Facebook.")
    app_token = login_or_register_with_facebook(profile)
    
    # 5. Coba login lagi dengan user yang sama untuk melihat skenario login.
    print("\n--- Mencoba login lagi dengan akun Facebook yang sama ---")
    app_token_2 = login_or_register_with_facebook(profile)
    
    print("\nDatabase user kita sekarang (tidak ada user baru yang dibuat):")
    print(json.dumps(user_database, indent=2))