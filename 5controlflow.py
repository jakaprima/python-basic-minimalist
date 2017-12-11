#if
x = int(raw_input("masukkan inputan: ")) #input
if x < 10:
    print "x lebih kecil dari 10"
elif x == 3:
    print "x sama dengan 3"
else:
    print "yang lainnya"
# output x lebih kecil dari 10

#for
array1 = ['jaka', 'prima', 'maulana']
for x in array1:
	print x, len(x)
#output
#jaka 4
#prima 5
#maulana 7

#insert di loop pada spesifik index
for w in array1[:]: #copy ke semua
	if len(w) > 5:
		array1.insert(0, w)
#output : maulana, jaka, prima, maulana


