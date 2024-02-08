#map adalah function yang membawa 2 argument yaitu function dan urutan iterable/perulangan map(function, sequence)

def penjumlahan(args):
	return 15 + args

urutan = [20, 10, 50]

map(penjumlahan, urutan)
#[35,25,65] 

#kalo pake lambda
map(lambda args: 15+args, urutan)
