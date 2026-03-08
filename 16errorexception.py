try:
	2 + 's'
except TypeError: #tanpa TypeError juga bisa
	print("disana ada tipe error")
finally:
	# block lets you execute code, regardless of the result of the try- and except blocks.
	print("finally terprint") #tertulis apapun yang terjadi

try:
	f = open('testfile', 'r') #w akan berhasil #r akan error
	f.write('test write this')
except: # bisa pake IOError
	print('eror saat menulis ke file')
else:
	# block lets you execute code when there is no error.
	print('file ditulis dengan sukses')

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")