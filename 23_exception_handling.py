# TUTORIAL: Exception Handling (Menangani Error)
# Tujuannya: Agar program tidak crash/berhenti saat terjadi error, tapi memberikan pesan yang jelas.

def bagi_angka(a, b):
    try:
        # Blok kode yang mungkin menyebabkan error
        hasil = a / b
    except ZeroDivisionError:
        # Menangkap error jika dibagi 0
        print("Error: Tidak bisa membagi angka dengan nol!")
        return None
    except TypeError:
        # Menangkap error jika input bukan angka
        print("Error: Input harus berupa angka!")
        return None
    except Exception as e:
        # Menangkap error lain yang tidak terduga
        print(f"Terjadi error yang tidak diketahui: {e}")
        return None
    else:
        # Dijalankan HANYA jika TIDAK ada error
        print(f"Pembagian berhasil. Hasilnya: {hasil}")
        return hasil
    finally:
        # Selalu dijalankan, baik ada error maupun tidak (biasanya untuk cleanup/tutup koneksi)
        print("--- Operasi selesai ---\n")

# Contoh Penggunaan
print("Kasus 1: Normal")
bagi_angka(10, 2)

print("Kasus 2: Error Pembagian Nol")
bagi_angka(10, 0)

print("Kasus 3: Error Tipe Data")
bagi_angka(10, "a")

# Tips Project:
# Jangan pernah menggunakan 'try: ... except: pass' (silent error), 
# karena akan membuat debugging sangat sulit.

# Best Practice:
# Gunakan Exception spesifik (seperti ValueError, KeyError) daripada Exception umum.