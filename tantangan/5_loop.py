# Tujuan
# dalam tantangan ini kita akan menggunakan loop untuk membantu kita melakukan simple matematika.

# Tugas
# berikan sebuah integer, n, print pada pertama 10 multiple. setiap multiple n x i (dimana 1 < i < 10) harus di print pada line baru dalam form: n x i = hasil


# Input Format
# single integer n

# kendala/constraint
# 2 < n < 20

# Output Format
# print 10 barus dari output; setiap line i (dimana 1 < i < 10) mengandung hasil n x i dalam form n x i = hasil


# Sample Input
# 2

# Sample Output
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20



import sys

n = int(input('masukkan angka : '))

for i in range(1, 11):
	print("%i x %i = %i" % (n, i, n*i)) 