# Objective
# belajar perbedaan class dan instance ini adalah konsep Object oriented ini hanya enable dalam bahasa tertentu

# Tugas
# tulis class Orang dengan instance variable umur dan 
# constructor yang membawa integer InitialUmur sebagai parameter. 
# dan constructor harus assign InitialUmur ke umur. setelah konfirmasi argument terlewati sebagai InitialUmur adalah bukan negative;
# jika negative argument ter passed sebagai InitialUmur
# constructor harus set umur ke 0

# sebagai tambahan kamu harus tulis instance method:
# tahunBerlalu() harus increase umur instance by 1
# apakahSayaTua() harus digunakan untuk melakukan kondisi:
# jika umur < 13 print kamu muda 
# jika umur > 13 dan < 18 kamu dewasa
# lainnya kamu tua 

# untuk membantu kamu belajar dari contoh dan selesaikan tantangan ini, banyak kode melayani kamu, tetapi kamu akan tulis semua kedepannya. code yang terbuat setiap instance dari class Orang adalah main method.

# catatan: jangan buang atau alter/ubah potongan kode dalam editor.


# Input Format:
# input handle potongan kode dalam editor
# line pertama mengandung integer (nomor yang akan di test)
# dan urutan barus setiap mengandung integer menunjukkan instance dari Orang


# kendala
# 1 < T < 4 
# -5 < umur < 30

# Output Format
# selesaikan definisi layanan method dalam editor sehingga mereka bisa menspesifikasikan deskripsi diatas;


# Sample Input
# 4
# -1
# 10
# 16
# 18

# Sample Output
# umur tidak valid, setting umur ke 0.
# Kamu masih muda.
# Kamu masih muda.

# Kamu masih muda.
# Kamu dewasa

# Kamu dewasa
# Kamu sudah tua

# Kamu sudah tua
# Kamu sudah tua

# penjelasan:
# Test Case 0: (InitialUmur = -1)
# karena InitialUmur < 0 kode kita harus set umur ke 0 dan set print 'umur tidak valid...' pesan yang diikuti dengan pesan muda. 3 tahun pass dan umur=3, sehingga kita print pesan muda lagi

# Test Case 1: (initialUmur = 10)
# karena kode kita harus < 13 print Orang yang muda. 3 taun pass dan umur=13 sehingga kita print Orang adalah masih muda.

# Test Case 2: (initialUmur = 16)
# karena 13 < initialUmur < 18, kode kita harus print Orang sebagai anak muda. 3 tahun pass dan umur 19, sehingga kita print Orang itu tua 

# Test Case 3: (initialUmur = 18)
# karena inisialisasi > 18, kode kita harus print Orang itu tua. 2 tahun pass dan Orang masih tua pada umur 21, jadi kita print pesan tua lagi 

# line tambahan pada akhir output harus ada disana dan terpotong sebelum dibandingkan test case expected output. jika kamu gagal challange ini, check logika kamu dan review print statement untuk menjelaskan error

class Orang(object):
    def __init__(self, inputUmur):
        # tambahkan code tambahan untuk menjalankan pengecekkan pada initialUmur\
        if inputUmur < 0:
            print("umur tidak valid, setting umur ke 0.")
            self.umur = 0
        else:
            self.umur = inputUmur

    def apakahSayaTua(self):
        # lakukan komputasi dan print statement yang benar
        if self.umur < 13:
            pesan = 'Kamu masih muda.'
        elif self.umur >= 13 and self.umur < 18:
            pesan = 'Kamu dewasa'
        elif self.umur >= 18:
            pesan = 'Kamu sudah tua'
        return pesan


    def tahunBerlalu(self):
        self.umur += 1


x = int(input())
for i in range(0, x):
    inputUmur = int(input("masukkan umur anda? "))

    instance = Orang(inputUmur)
    # print('isi instance', instance.apakahSayaTua())
    print(instance.apakahSayaTua())

    for i2 in range(0, 3):
        instance.tahunBerlalu()
    print(instance.apakahSayaTua())

