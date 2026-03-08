# TUTORIAL: Google Login dengan `requests-oauthlib`
# Google menggunakan standar OpenID Connect (OIDC) di atas OAuth 2.0.
# Alurnya mirip dengan Facebook, tapi endpoint dan scope-nya berbeda.

# Prasyarat: pip install requests requests-oauthlib

from requests_oauthlib import OAuth2Session
import os

# --- Konfigurasi Aplikasi (Dari Google Cloud Console) ---
# 1. Buka https://console.cloud.google.com/
# 2. Buat Project -> APIs & Services -> Credentials -> Create OAuth Client ID
# 3. Set Authorized redirect URIs ke URL callback Anda (misal: https://your-app.com/callback)

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "your_google_client_id")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "your_google_client_secret")
REDIRECT_URI = "https://your-app.com/callback"

# Endpoint standar Google
AUTHORIZATION_BASE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

# Scope standar untuk login Google
# 'openid': Wajib untuk OIDC
# 'email': Mengakses alamat email user
# 'profile': Mengakses nama dan foto profil
SCOPE = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile"
]

# --- 1. Langkah Awal: Mengarahkan User ke Google ---
def get_google_login_url():
    """
    Membuat URL login Google.
    """
    google = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)
    
    # access_type="offline" penting jika kita butuh Refresh Token
    # prompt="consent" memaksa user melihat layar persetujuan lagi (berguna untuk debug)
    authorization_url, state = google.authorization_url(
        AUTHORIZATION_BASE_URL,
        access_type="offline",
        prompt="consent"
    )
    
    print(f"1. Arahkan user ke URL ini: \n{authorization_url}")
    print(f"2. Simpan 'state' ini di session user: {state}")
    return authorization_url, state


# --- 2. Langkah Callback: Menukar Kode dengan Token ---
def google_callback_handler(authorization_response_url, state_from_session):
    """
    Dipanggil setelah user login di Google dan dialihkan kembali.
    """
    google = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=state_from_session)
    
    print("\n--- Menukar Authorization Code dengan Access Token ---")
    
    try:
        # Mocking untuk demo jika kredensial dummy
        if CLIENT_ID == "your_google_client_id":
            print("(Simulasi) Fetching token dari Google...")
            token = {
                "access_token": "mock_google_access_token_abc",
                "token_type": "Bearer",
                "expires_in": 3599,
                "refresh_token": "mock_refresh_token_xyz",
                "id_token": "mock_id_token_jwt_string" # Berisi info user (OIDC)
            }
        else:
            # Fetch token asli
            token = google.fetch_token(
                TOKEN_URL,
                client_secret=CLIENT_SECRET,
                authorization_response=authorization_response_url
            )
            
        print(f"Access Token: {token['access_token']}")
        
        # Google juga mengembalikan 'id_token' (JWT) yang berisi info user.
        # Kita bisa decode JWT itu atau panggil endpoint userinfo.
        print(f"ID Token (JWT): {token.get('id_token', 'Tidak ada (mock)')}")
        
        return google, token
        
    except Exception as e:
        print(f"Error saat fetch token: {e}")
        return None, None

if __name__ == "__main__":
    print("--- Demo Google OAuth 2.0 ---")
    login_url, state = get_google_login_url()
    dummy_callback = f"{REDIRECT_URI}?code=valid_google_code&state={state}"
    session, token = google_callback_handler(dummy_callback, state)