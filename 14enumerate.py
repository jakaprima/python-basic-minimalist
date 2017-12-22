# mengijinkan kamu tetap dalam count dari perulangan melewati object. mengembalikan tuple dalma form(count,element)

# sama dengan
# def enumerate(sequence, start=0):
# 	n = start
# 	for elem in sequence:
# 		yield n, elem
# 		n += 1

list = ['a','b','c']
i = 0
for item in list:
	print i
	print item
	i += 1
# 0
# a
# 1
# b
# 2
# c

for i,item in enumerate(list): #jadi bisa pake i
	if i >= 2:
		break
	else:
		print item #a,b

