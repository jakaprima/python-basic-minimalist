# TUTORIAL: concurrent.futures (ThreadPoolExecutor vs ProcessPoolExecutor)
# Module `concurrent.futures` menyediakan interface level tinggi untuk menjalankan tugas
# secara asinkron menggunakan thread atau proses.

import concurrent.futures
import time
import os

# --- 1. CPU-Bound Task ---
# Tugas berat yang memakan CPU (misal: faktorial angka besar)
def cpu_bound_task(n):
    # pid = os.getpid()
    # print(f"CPU Task {n} running on PID {pid}")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# --- 2. I/O-Bound Task ---
# Tugas yang menunggu (misal: request network, sleep)
def io_bound_task(n):
    # pid = os.getpid()
    # print(f"IO Task {n} running on PID {pid}")
    time.sleep(2) # Simulasi menunggu 2 detik
    return f"Selesai {n}"

def run_demo():
    # Angka besar untuk membebani CPU (hitung faktorial 20.000)
    angka_cpu = [20000, 20000, 20000] 
    angka_io = [1, 2, 3]

    print("--- 1. ThreadPoolExecutor (Best for I/O) ---")
    start = time.time()
    # ThreadPoolExecutor menggunakan Thread.
    # Cocok untuk I/O bound karena saat satu thread menunggu (sleep/network),
    # thread lain bisa jalan.
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(io_bound_task, angka_io))
    
    print(f"Waktu ThreadPool (I/O): {time.time() - start:.4f} detik (Harusnya ~2s)")
    
    print("\n--- 2. ProcessPoolExecutor (Best for CPU) ---")
    start = time.time()
    # ProcessPoolExecutor menggunakan Process (Core CPU terpisah).
    # Cocok untuk CPU bound karena setiap proses punya Python Interpreter sendiri,
    # jadi tidak terhalang GIL.
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cpu_bound_task, angka_cpu))

    print(f"Waktu ProcessPool (CPU): {time.time() - start:.4f} detik (Cepat)")

    print("\n--- 3. Comparison (Wrong Tool) ---")
    # Coba pakai Thread untuk CPU bound (Akan lambat karena GIL)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cpu_bound_task, angka_cpu))
    print(f"Waktu ThreadPool (CPU - Salah Guna): {time.time() - start:.4f} detik (Lebih lambat)")

if __name__ == "__main__":
    run_demo()