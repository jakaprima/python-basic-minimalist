# TUGAS

# berikan integer
# lalu aplikasikan aksi kondisi
# jika n itu odd print Aneh
# jika n itu even dan inclusive/termasuk range dari 2 sampe 5, print tidak Aneh
# jika n itu even dan termasuk range dari 6 sampe 20 print Aneh
# jika n itu lebih dari 20 print tidak aneh

# selesaikan potongan layanan code dalam editor dan print whether/apakah atau tidak aneh


# Input Format
# satu baris mengandung positive integer variable n

# kecuali = 1 < n < 100

# output Format
# Print Aneh jika number aneh; sebaliknya print tidak aneh


# Sample Input = 3
# output = aneh

# Sample Input = 24
# output = tidak aneh

N = int(input("masukkan input ").strip())

if N >= 2 and N <= 5:
	if N % 2 == 0:
		print('tidak aneh')
	else:
		print('aneh')
elif N > 5 and N < 21:
	if N % 2 == 0:
		print('aneh')
	else:
		print('tidak aneh')
else:
	if N % 2 == 1
		print('tidak aneh')
	else:
		print('aneh')





