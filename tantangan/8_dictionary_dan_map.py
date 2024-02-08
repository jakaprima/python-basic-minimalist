# Tujuan/objective
# belajar key-value pair mapping menggunakan Map atau dictionary struktur data.

# Tugas
# berikan (n) nama dan nomor_telpon, assemble/himpunan buku telpon yang mapping nama teman dari nomor telpon masing". selanjutnya kamu akan diberikan nomor yang tidak diketahui sebagai nama ke query phone book kamu.

# setiap (nama) queried print asosiasi entry dari buku telpon kamu pada baris baru dalam form nama=nomortelpon; jika masukkan untuk (nama) tidak ditemukan print tidak ditemukan dan sebaliknya

# Catatan: buku telpon kamu harus sebuah struktur data Dictionary/Map/HashMap. 


# Input Format
# baris pertama mengandung integer (n) menunjukkan nomor dari masukkan dalam buku telpon. 

# setiap urutan baris mendeskripsikan entry dari form pemisah-spasi 
# dalam satu baris. value pertama adalah nama teman, dan value kedua adalah digit nomor telpon. 

# setelah baris (n) dalam masukkan buku telpon, disana terdapat baris nomor yang tidak diketahui dari queries. setiap line (query) mengandung nama untuk di look up, dan kamu harus melanjutkan membaca baris sampai tidak ada input lagi 

# Catatan: nama mengandung huruf kecil 

# kendala:
# 1 < n < 10pangkat5
# 1 < queries > 10pangkat5

# Output Format
# pada baris baru setiap query print tidak ditemukan jika nama tidak sesuai/corresponding entry dalam buku telpon; otherwise/sebaliknya print nama lengkap dan nomorTelpon dalam format nama=nomorTelpon

# Contoh Input

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

# Contoh Output

# sam=99912222
# Not found
# harry=12299933

# Penjelasan
# kita menambahkan n = 3 (key, Value) pairs ke map kita sehingga terlihat seperti ini 

# bukuTelpon = {(sam,99912222), (tom, 11122222), (harry, 12299933)}

# selanjutnya kita proses setiap query dan print key=value jika queried key ditemukan dalam map; otherwise/sebaliknya, kita print tidak ditemukan

# Query 0: sam
# sam adalah hsatu dari kunci dalam dictionary jadi kita print sam=99912222

# Query 1: edward 
# Edward bukan salah satu kunci dari dictionary kita, jadi kita print tidak ditemukan.

# Query 2: harry 
# Harry adalah hsatu dari kunci dalam dictionary jadi kita print harry=12299933.

i = int(input())
data={}

for x in range(0, i):
	array = input().split(" ")
	data[array[0]]=array[1]

for y in range(0, i):
	i2 = input()
	if i2 in data:
		print( i2 + "=" + data[i2])
	else:
		print("Not found")

