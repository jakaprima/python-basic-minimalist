# TUTORIAL: Menjalankan Command Eksternal (subprocess)
# Module `subprocess` memungkinkan kita menjalankan program lain (seperti perintah terminal)
# dari dalam script Python.

import subprocess
import platform

# --- 1. Cara Dasar: subprocess.run() ---
# Ini adalah cara yang direkomendasikan untuk sebagian besar kasus.
# Gunakan list ["command", "arg1"] untuk keamanan (menghindari Shell Injection).

print("--- 1. Menjalankan Perintah Sederhana ---")

# Contoh: Cek versi python
print("Menjalankan 'python --version'...")
subprocess.run(["python", "--version"])


# --- 2. Mengambil Output (Stdout) ---
# Secara default, output langsung muncul di terminal.
# Jika ingin menyimpan output ke variabel, gunakan `capture_output=True`.

print("\n--- 2. Mengambil Output ke Variabel ---")

result = subprocess.run(
    ["python", "--version"], 
    capture_output=True, # Tangkap output (stdout dan stderr)
    text=True            # Decode byte ke string otomatis (biar ga jadi b'...')
)

print(f"Return Code: {result.returncode}") # 0 artinya sukses
print(f"Output (stdout): {result.stdout.strip()}")
# print(f"Error (stderr): {result.stderr}") 


# --- 3. Handling Error ---
# Jika command gagal (return code != 0), kita bisa mendeteksinya.

print("\n--- 3. Handling Error ---")
try:
    # `check=True` akan raise CalledProcessError jika command gagal
    subprocess.run(["python", "--perintah-salah"], check=True, capture_output=True)
except subprocess.CalledProcessError as e:
    print(f"Terjadi Error! Return code: {e.returncode}")


# --- 4. Shell=True (Gunakan dengan Hati-hati!) ---
# shell=True dibutuhkan jika ingin menggunakan fitur shell seperti pipe (|), redirect (>),
# atau command bawaan shell (seperti 'dir' di Windows atau 'ls' di Linux).

print("\n--- 4. Shell=True ---")

# Tentukan command berdasarkan OS
perintah_list = "dir" if platform.system() == "Windows" else "ls -l"

print(f"Menjalankan '{perintah_list}' dengan shell=True:")
# Karena shell=True, kita bisa pass string langsung (bukan list).
subprocess.run(perintah_list, shell=True)

# PERINGATAN KEAMANAN:
# Jangan gunakan shell=True jika input command berasal dari user (raw_input),
# karena rentan terhadap serangan "Shell Injection".