#reduce(function, sequence) berlanjut mengaplikasikan fungsi ke urutan
#berbeda sama map dia akan hanya mereturn 1 hasil
#jadi akan seperti ini [(1,2),3),4),5)] hasil sebelumnya akan execute dengan hasil selanjutnya dari function didalam args

def penjumlahan(args1, args2):
	return args1 + args2

urutan = [1,2,3,4,5]
reduce(penjumlahan, urutan)
#15