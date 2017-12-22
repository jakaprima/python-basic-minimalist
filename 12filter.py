#filter rumus filter(function, list) melayani kenyamanan dalam filter keluaran dari semua element dari perulangan dimana untuk function yang mereturn true, function butuh boolean

# urutan = [[1,'string1',True],[4,'string2',False]]
urutan = [1,2,3,1]

def kategori1(args):
	if args == 1:
		return True

urutanbaru = filter(kategori1, urutan)
print urutanbaru #[1, 1]
	