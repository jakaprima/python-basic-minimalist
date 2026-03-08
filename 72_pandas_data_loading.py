# TUTORIAL: Membaca Data dengan Pandas (CSV, Excel, JSON, API)
# Pandas adalah library analisis data yang sangat powerful.
# Fungsi utamanya adalah mengubah data mentah menjadi "DataFrame" (tabel).

# Prasyarat: pip install pandas openpyxl requests

import pandas as pd
import os
import requests

# --- SETUP DATA DUMMY ---
# Kita buat file dummy dulu agar script ini bisa dijalankan langsung tanpa download file eksternal.

csv_file = "dummy_data.csv"
json_file = "dummy_data.json"
excel_file = "dummy_data.xlsx"

def create_dummy_files():
    # Membuat DataFrame sederhana
    data = {
        "Nama": ["Andi", "Budi", "Caca", "Deni"],
        "Umur": [25, 30, 22, 28],
        "Kota": ["Jakarta", "Bandung", "Surabaya", "Jakarta"],
        "Gaji": [10000000, 8000000, 9000000, 12000000]
    }
    df = pd.DataFrame(data)
    
    # 1. Simpan ke CSV
    df.to_csv(csv_file, index=False)
    
    # 2. Simpan ke JSON
    df.to_json(json_file, orient="records", indent=4)
    
    # 3. Simpan ke Excel (Butuh library 'openpyxl')
    try:
        df.to_excel(excel_file, index=False)
    except ImportError:
        print("Warning: Library 'openpyxl' belum terinstall. Skip pembuatan Excel.")

if __name__ == "__main__":
    create_dummy_files()
    
    print("--- 1. Membaca CSV ---")
    if os.path.exists(csv_file):
        # pd.read_csv adalah fungsi paling umum
        df_csv = pd.read_csv(csv_file)
        print(df_csv)
        print(f"Info: {df_csv.shape[0]} baris, {df_csv.shape[1]} kolom")
    
    print("\n--- 2. Membaca JSON ---")
    if os.path.exists(json_file):
        # orient='records' biasa digunakan untuk list of objects (standar API)
        df_json = pd.read_json(json_file, orient='records')
        print(df_json.head(2)) # Tampilkan 2 baris pertama saja
        
    print("\n--- 3. Membaca Excel ---")
    if os.path.exists(excel_file):
        try:
            # pd.read_excel butuh 'openpyxl'
            df_excel = pd.read_excel(excel_file)
            # Filter data: Tampilkan yang gajinya di atas 9 juta
            high_salary = df_excel[df_excel['Gaji'] > 9000000]
            print("Gaji > 9 Juta:")
            print(high_salary)
        except ImportError:
            print("Error: Install 'openpyxl' untuk membaca Excel: pip install openpyxl")

    print("\n--- 4. Membaca dari API ---")
    # Kita gunakan API publik JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        print(f"Mengambil data dari {url}...")
        response = requests.get(url)
        response.raise_for_status()
        data_api = response.json() # Ini biasanya list of dictionaries
        
        # Pandas pintar, bisa langsung convert list of dicts ke DataFrame
        df_api = pd.DataFrame(data_api)
        
        # Tampilkan kolom tertentu saja agar rapi
        print(df_api[['id', 'name', 'email', 'website']].head(3))
        
    except Exception as e:
        print(f"Gagal mengambil data API: {e}")

    # Cleanup (Hapus file dummy)
    # if os.path.exists(csv_file): os.remove(csv_file)
    # if os.path.exists(json_file): os.remove(json_file)
    # if os.path.exists(excel_file): os.remove(excel_file)