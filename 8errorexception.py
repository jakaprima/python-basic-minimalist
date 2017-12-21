try:
	2 + 's'
except TypeError: #tanpa TypeError juga bisa
	print "disana ada tipe error"
finally:
	print "finally terprint" #tertulis apapun yang terjadi

try:
	f = open('testfile', 'r') #w akan berhasil #r akan error
	f.write('test write this')
except: # bisa pake IOError
	print 'eror saat menulis ke file'
else:
	print 'file ditulis dengan sukses'
