# TUTORIAL: Python Decorators
# Decorator adalah fitur powerful untuk memodifikasi perilaku function atau method
# tanpa mengubah kode di dalam function itu sendiri.
# Analogi: Seperti membungkus kado. Isinya sama, tapi kemasannya (behavior) dipercantik.

import time
import functools

# --- 1. Struktur Dasar Decorator ---
# Decorator adalah function yang menerima function lain, dan mengembalikan wrapper.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Memanggil fungsi: {func.__name__}")
        # Menjalankan fungsi asli
        result = func(*args, **kwargs)
        print(f"[LOG] Selesai memanggil: {func.__name__}")
        return result
    return wrapper

# --- 2. Contoh Praktis: Pengukur Waktu (Timer) ---
# Sangat berguna untuk profiling performa kode.

def timer_decorator(func):
    """Decorator untuk menghitung waktu eksekusi function."""
    
    # @functools.wraps(func) adalah best practice.
    # Ini memastikan metadata function asli (nama, docstring) tidak hilang tertimpa wrapper.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time() # Catat waktu mulai
        
        result = func(*args, **kwargs) # Jalankan function asli
        
        end_time = time.time() # Catat waktu selesai
        duration = end_time - start_time
        
        print(f"⏱️  Function '{func.__name__}' berjalan selama {duration:.4f} detik.")
        return result
    return wrapper

# --- 3. Cara Menggunakan Decorator (@) ---

@log_decorator
def sapa(nama):
    print(f"Halo, {nama}!")

@timer_decorator
def operasi_berat(n):
    """Melakukan perhitungan kuadrat dalam loop."""
    print(f"Memulai kalkulasi {n} kali...")
    total = sum(i**2 for i in range(n))
    return total

# --- 4. Demo Eksekusi ---

if __name__ == "__main__":
    print("--- Demo 1: Logging Decorator ---")
    sapa("Budi")
    # Output:
    # [LOG] Memanggil fungsi: sapa
    # Halo, Budi!
    # [LOG] Selesai memanggil: sapa

    print("\n--- Demo 2: Timer Decorator ---")
    hasil = operasi_berat(1_000_000)
    print(f"Hasil kalkulasi: {hasil}")
    
    # Bukti bahwa metadata terjaga (karena functools.wraps)
    print(f"\nInfo Function: {operasi_berat.__name__}")
    print(f"Docstring: {operasi_berat.__doc__}")