#generator = fungsi yang mengijinkan menulis fungsi yang mengembalikan value dan nanti akan dipakai untuk mengambil dimana dia pergi

#generate sequence values berkalikali
#perbedaannya menggunakan yield statement

#hasilnya menjadi object yang support iteratisi protocol
def generator1(n):
	for nomor in range(n):
		yield nomor**2
for x in generator1(10):
	print x 
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

def generator2(n):
	a = 1
	b = 1
	for nomor in range(n):
		yield a
		a, b = b, a+b
for nomor in generator2(7):
	print nomor
# 0+1=1, 1+1=2, 2+1=3, 3+2=5, 5+3=8, 8+5=13
# 1,1,2,3,5,8,13

