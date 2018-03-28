# objective/tujuan
# belajar struktur data array.

# Tugas
# berikan array A dari N integer
# print element dalam reverse order dalam satu baris dengan pemisah spasi nomor

# Input Format
# pada baris pertama mengandung integer N (size dari array kita)
# baris kedua mengandung pemisah spasi integer mendeskripsikan array elements. 

# kendala
# 1 < N < 1000
# 1 < Ai < 10000 dimana Ai adalah i integer dalam array

# Output
# print element array A dalam reverse order dalam satu baris pemisah number

# Sample Input
# 4
# 1 4 3 2

# Sample Output
# 2 3 4 1

import sys


N = int(input().strip())
A = input().split()

print(' '.join(A[::-1]))
