# Tujuan
# meluaskan pengetahuan dari string dan melakukan kombinasi dengan apa yang sudah kita pelajari tentang loops.

# Tugas
# berikan string, S, dan length N dimana terindex dari 0 ke N - 1, print setiap even-index dan odd-index karakter sebagai 2 pemisah spasi string dalam single line (liat contoh di bawah)

# catatan: 0 mengacu pada even index

# input Format
# baris pertama mengandung integer, T (nomor dari contoh test)
# setiap baris i dari T berurutan line mengandung string S. 

# KENDALA:
# 1 < T < 10
# 2 < length dari S < 10000

# output format:
# untuk setiap string Sj (dimana 0 < j < T - 1), print Sj event-indexed karakter diikuti dengan spasi, diikuti dengan odd-index karakter

# sampel input
# 2
# Hacker
# Rank

# sampel output
# Hce akr
# Rn ak


# PENJELASAN
# test case 0: S = "Hacker"
# S[0] = "H"
# S[1] = "a"
# S[2] = "c"
# S[3] = "k"
# S[4] = "e"
# S[5] = "r"

# even mengindikasikan 0,2,4 dan odd 1,3,5

# kita print satu baris dari 2 spasi-pemisah string;
# string pertama mengandung urutan karakter dari S event indices/menunjuk (Hce), dan string kedua mengandung ordered karakter dari S odd indices (akr)

# TEST CASE 1: S = "Rank"
# S[0] = "R"
# S[1] = "a"
# S[2] = "n"
# S[3] = "k"

# even indices 0 dan 2 dan odd indices 1 dan 3 kita print single line dari 2 spasi-pemisah string; string pertama mengandung ordered karakter dari S even indices (Rn) dan string kedua ordered karakter dari S odd indices(ak)


# kalimat = ''

# for i in range(int(input())):
# 	input_data = str(input())
# 	input_data_array = list(input_data)
# 	if i % 2 == 0:
# 		kalimat += input_data_array[i]
# 		# kalimat.append(input_data_array[i])
# 		print('isi', kalimat)
# 	else:
# 		kalimat += input_data_array[i]
# 		print('isi2', input_data_array[i])

# print('kalimat', kalimat)

# paling simple
for i in range(int(input())):
	s = input();
	x = print(*[
		"".join(s[::2]),
		"".join(s[1::2])
		]
	)

