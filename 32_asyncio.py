# TUTORIAL: Asynchronous Programming (Async/Await)
# Asyncio digunakan untuk menulis kode konkuren menggunakan sintaks async/await.
# Sangat berguna untuk operasi I/O-bound (menunggu database, API, file) agar tidak memblokir eksekusi program.

import asyncio
import time

# --- 1. Fungsi Synchronous (Biasa) ---
# Fungsi ini "Blocking". Program akan diam menunggu sleep selesai sebelum lanjut.
def seduh_kopi_sync():
    print("Sync: Mulai seduh kopi...")
    time.sleep(2) # Simulasi proses lama (2 detik) menggunakan time.sleep
    print("Sync: Kopi siap!")
    return "Kopi Hitam"

def panggang_roti_sync():
    print("Sync: Mulai panggang roti...")
    time.sleep(2)
    print("Sync: Roti siap!")
    return "Roti Bakar"

def sarapan_sync():
    start = time.time()
    print("--- Mulai Sarapan (Sync) ---")
    # Dijalankan berurutan: Kopi selesai dulu, baru Roti mulai.
    kopi = seduh_kopi_sync()
    roti = panggang_roti_sync()
    
    end = time.time()
    print(f"Selesai: Makan {roti} minum {kopi}")
    print(f"Total Waktu Sync: {end - start:.2f} detik (Harusnya ~4 detik)\n")

# --- 2. Fungsi Asynchronous (Async) ---
# Fungsi didefinisikan dengan `async def`.
# `await` digunakan untuk menunggu proses (coroutine) lain tanpa memblokir event loop.

async def seduh_kopi_async():
    print("Async: Mulai seduh kopi...")
    await asyncio.sleep(2) # Non-blocking sleep (asyncio.sleep), CPU bisa kerja lain saat menunggu ini.
    print("Async: Kopi siap!")
    return "Kopi Hitam"

async def panggang_roti_async():
    print("Async: Mulai panggang roti...")
    await asyncio.sleep(2)
    print("Async: Roti siap!")
    return "Roti Bakar"

async def sarapan_async():
    start = time.time()
    print("--- Mulai Sarapan (Async) ---")
    
    # Menjalankan task secara concurrent (bersamaan)
    # Kita gunakan asyncio.gather untuk menjadwalkan keduanya sekaligus
    print("Async: Mengerjakan keduanya sekaligus...")
    hasil = await asyncio.gather(seduh_kopi_async(), panggang_roti_async())
    
    kopi, roti = hasil
    end = time.time()
    print(f"Selesai: Makan {roti} minum {kopi}")
    print(f"Total Waktu Async: {end - start:.2f} detik (Harusnya ~2 detik)")
    print("(Lebih cepat karena berjalan paralel saat menunggu)")

if __name__ == "__main__":
    # 1. Jalanin Sync
    sarapan_sync()
    
    # 2. Jalanin Async
    # asyncio.run() adalah cara standar menjalankan top-level entry point untuk kode async (Python 3.7+)
    asyncio.run(sarapan_async())