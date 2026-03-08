# TUTORIAL: Bekerja dengan Tanggal dan Waktu (datetime)
# `datetime` adalah modul standar Python untuk memanipulasi tanggal dan waktu.

import datetime

# 1. Mendapatkan Waktu Saat Ini
sekarang = datetime.datetime.now()
print(f"Waktu sekarang: {sekarang}")

# 2. Membuat Objek datetime Spesifik
ulang_tahun = datetime.datetime(2024, 8, 17, 10, 30, 0)
print(f"Ulang tahun di: {ulang_tahun}")

# 3. Formatting Tanggal menjadi String (strftime)
# %Y: Tahun (2024), %m: Bulan (08), %d: Hari (17)
# %H: Jam (10), %M: Menit (30), %S: Detik (00)
# %A: Nama hari (Saturday), %B: Nama bulan (August)
print(f"Format Indonesia: {sekarang.strftime('%d-%m-%Y %H:%M')}")
print(f"Format Lengkap: {sekarang.strftime('%A, %d %B %Y')}")

# 4. Parsing String menjadi Tanggal (strptime)
string_tanggal = "01-01-2025"
tanggal_objek = datetime.datetime.strptime(string_tanggal, "%d-%m-%Y")
print(f"Objek dari string: {tanggal_objek}")

# 5. Operasi dengan timedelta (Selisih Waktu)
satu_minggu_lagi = sekarang + datetime.timedelta(weeks=1)
kemarin = sekarang - datetime.timedelta(days=1)
print(f"Satu minggu dari sekarang: {satu_minggu_lagi.strftime('%d %B %Y')}")
print(f"Kemarin adalah hari: {kemarin.strftime('%A')}")