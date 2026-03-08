# TUTORIAL: Menggabungkan Requests (Sync) dengan Asyncio
# Masalah: Library 'requests' itu blocking. Jika dipakai langsung, async tidak berguna.
# Solusi: Bungkus 'requests' dalam ThreadPoolExecutor agar jalan di thread terpisah.

import asyncio
import requests
import time

URL = "https://jsonplaceholder.typicode.com/todos/1"

# 1. Ini fungsi biasa (Synchronous/Blocking)
def ambil_data_sync(urutan):
    print(f"Request {urutan}: Mulai mengirim...")
    # Ini akan memblokir CPU jika tidak dipindah ke thread lain
    resp = requests.get(URL) 
    print(f"Request {urutan}: Selesai! Status {resp.status_code}")
    return resp.json()

async def main():
    # Mendapatkan event loop yang sedang berjalan
    loop = asyncio.get_running_loop()
    
    print("--- Mulai: Menjalankan requests secara concurrent ---")
    start_time = time.time()

    # 2. Menyiapkan Futures (Tugas masa depan)
    # loop.run_in_executor(Executor, Fungsi, Argumen...)
    # Executor=None artinya pakai default ThreadPoolExecutor
    
    tugas1 = loop.run_in_executor(None, ambil_data_sync, 1)
    tugas2 = loop.run_in_executor(None, ambil_data_sync, 2)
    tugas3 = loop.run_in_executor(None, ambil_data_sync, 3)

    # 3. Menunggu semua tugas selesai (Await)
    # asyncio.gather menunggu semua future selesai secara paralel
    hasil1, hasil2, hasil3 = await asyncio.gather(tugas1, tugas2, tugas3)

    end_time = time.time()
    
    print(f"\nTotal Waktu: {end_time - start_time:.2f} detik")
    print("Analisa: Jika 1 request butuh 0.5 detik, 3 request harusnya 1.5 detik.")
    print("Tapi karena concurrent, total waktu hanya sekitar ~0.5 - 0.7 detik.")

if __name__ == "__main__":
    asyncio.run(main())

# --- KESIMPULAN: Requests vs Aiohttp ---
# 1. Requests + run_in_executor:
#    - Kelebihan: Tidak perlu belajar library baru, kode lama bisa dipakai.
#    - Kekurangan: Menggunakan Thread (lebih berat di memori dibanding native async).
#      Kurang cocok untuk ribuan request sekaligus.

# 2. Aiohttp / Httpx (Native Async):
#    - Kelebihan: Sangat ringan, menggunakan non-blocking sockets. Bisa handle ribuan koneksi.
#    - Kekurangan: Syntax berbeda (harus pakai `async with session.get(...)`).
#    - Gunakan ini jika membangun aplikasi High Performance.
