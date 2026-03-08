# TUTORIAL: Facebook Login dengan `requests-oauthlib`
# Library `requests-oauthlib` sangat memudahkan proses OAuth 2.0.
# Ia menangani pembuatan URL otorisasi dan penukaran token secara otomatis.

# Prasyarat: pip install requests requests-oauthlib

from requests_oauthlib import OAuth2Session
import os

# --- Konfigurasi Aplikasi (Dari Developer Console Facebook) ---
# Di aplikasi nyata, simpan ini di environment variables!
CLIENT_ID = os.getenv("FB_CLIENT_ID", "your_app_id")
CLIENT_SECRET = os.getenv("FB_CLIENT_SECRET", "your_app_secret")
REDIRECT_URI = "https://your-app.com/callback"

# Endpoint standar Facebook
AUTHORIZATION_BASE_URL = "https://www.facebook.com/dialog/oauth"
TOKEN_URL = "https://graph.facebook.com/oauth/access_token"


# --- 1. Langkah Awal: Mengarahkan User ke Facebook ---
def get_login_url():
    """
    Membuat URL login Facebook. User akan diarahkan ke sini.
    """
    # Scope adalah izin yang kita minta (misal: email)
    facebook = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=["email"])
    
    # authorization_url: URL halaman login Facebook
    # state: String acak untuk mencegah serangan CSRF (disimpan otomatis oleh library)
    authorization_url, state = facebook.authorization_url(AUTHORIZATION_BASE_URL)
    
    print(f"1. Arahkan user ke URL ini: \n{authorization_url}")
    print(f"2. Simpan 'state' ini di session user: {state}")
    return authorization_url, state


# --- 2. Langkah Callback: Menukar Kode dengan Token ---
def callback_handler(authorization_response_url, state_from_session):
    """
    Dipanggil setelah user login dan dialihkan kembali ke aplikasi kita.
    URL callback akan berisi '?code=...' dan '&state=...'.
    """
    
    # Re-create session dengan state yang disimpan sebelumnya
    facebook = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, state=state_from_session)
    
    print("\n--- Menukar Authorization Code dengan Access Token ---")
    
    # Library otomatis mengambil 'code' dari URL, mengirim POST ke TOKEN_URL,
    # dan memparsing JSON response menjadi token dictionary.
    # Di dunia nyata, ini butuh koneksi internet valid ke Facebook.
    try:
        # Karena ini demo tanpa server nyata, kita mock bagian fetch_token jika kredensial dummy
        if CLIENT_ID == "your_app_id":
            print("(Simulasi) Fetching token...")
            token = {
                "access_token": "mock_access_token_123",
                "token_type": "Bearer",
                "expires_in": 5183999
            }
        else:
            token = facebook.fetch_token(
                TOKEN_URL,
                client_secret=CLIENT_SECRET,
                authorization_response=authorization_response_url
            )
            
        print(f"Access Token berhasil didapat: {token['access_token']}")
        return facebook, token
        
    except Exception as e:
        print(f"Error saat fetch token: {e}")
        return None, None


# --- Demo Alur ---
if __name__ == "__main__":
    print("--- Demo OAuth 2.0 dengan requests-oauthlib ---")
    
    # 1. Generate URL
    login_url, state = get_login_url()
    
    # 2. Simulasi Callback (User kembali dengan URL ini)
    dummy_callback_url = f"{REDIRECT_URI}?code=valid_code_123&state={state}"
    session, token = callback_handler(dummy_callback_url, state)