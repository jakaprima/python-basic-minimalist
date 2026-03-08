# TUTORIAL: Mengambil Data dari API dengan 'requests'
# API (Application Programming Interface) adalah cara program berkomunikasi satu sama lain.
# Kita akan menggunakan API publik gratis dari JSONPlaceholder.

import requests
import json

def get_todo_by_id(todo_id: int):
    """
    Mengambil data 'todo' dari API berdasarkan ID-nya.
    """
    # URL dari endpoint API yang akan kita akses
    api_url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    
    logging.info(f"Mengirim request GET ke: {api_url}")
    
    try:
        # Melakukan request GET ke URL
        response = requests.get(api_url)
        
        # Memeriksa apakah request berhasil (status code 200 OK)
        response.raise_for_status() # Ini akan raise error jika status code bukan 2xx
        
        # Mengubah response JSON menjadi dictionary Python
        data = response.json()
        logging.info("Request berhasil dan data JSON telah di-parse.")
        return data
        
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error terjadi: {http_err}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Error lain terjadi: {err}")
    
    return None

# Contoh penggunaan
todo_item = get_todo_by_id(1)
if todo_item:
    print("\n--- Data Todo Ditemukan ---")
    print(f"User ID: {todo_item.get('userId')}")
    print(f"Judul: {todo_item.get('title')}")
    print(f"Selesai: {'Ya' if todo_item.get('completed') else 'Belum'}")