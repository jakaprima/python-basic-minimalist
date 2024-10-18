
# attribute = karakter dari object
# method = operasi kinerja yang dapat di lakukan dengan object
#self.attribute = something
# __init__() = spesial method initialize attribute

class sample(object):
	pass
x = sample()
type(x) #__main__.Sample


class orang(object):
	#class object attr
	category = 'orang' # class variable yang dishare semua instances/contoh

	def __init__(self, argument):
		self.var_a = argument # instance variable unique to each instance

	# def __str__(self):
	# 	digunakan jika ingin mengembalikan string di default ketika memanggil orang('jaka')
	# 	return f"{self.var_a}"

jaka = orang('jaka prima')
jaka.var_a # jaka prima
jaka.category # orang
# modify obj props / attr val
jaka.var_a = 'jaka edit'
print("edit:", jaka.var_a)

# object method
class lingkaran(object):
	pi = 3.14
	def __init__(self, radius=1):
		self.radius = radius
	def area(self):
		# method
		# self params hold current instance of the class
		return (self.radius**2) * lingkaran.pi
	def set_radius(self, radius_baru):
		# method
		self.radius = radius_baru
	def get_radius(self):
		# method
		return self.radius
c = lingkaran(radius = 10)
c.area() #314.0
c.radius # 10
c.set_radius(20) 
c.radius # 20
c.get_radius() #10


# ------------------------------------------------------------------- inheritence / hak waris
class ParentClass(object):
	def __init__(self):
		print('orang')

	def siapa(self):
		print('nama')

	def aksi(self):
		print('jalan')

		
class ChildClass(ParentClass):
	def __init__(self):
		ParentClass.__init__(self)
		print('saya bayi')
	def siapa(self):
		print('jaka')
	def aksi2(self):
		print('aksi 2')


d = ChildClass()
d # orang, saya bayi
d.siapa #jaka
d.aksi #jalan
d.aksi2 #minum



# contoh menggunakan super class
class ParentClass2():
	def __init__(self, fname):
		self.fname = fname

class ParentClass3():
	def __init__(self, lname):
		self.lname = lname

class ChildClass4(ParentClass2, ParentClass3):
	def __init__(self, fname, lname, age):
		# jika tanpa super maka harus inisialisasi seperti ini
		# self.fname = fname
		super().__init__(fname)
		# jika memiliki 2 parent class maka super() hanya memanggil class pertama
		# yang ke 2 ParentClass3 harus di panggil melalui ulang seperti berikut
		ParentClass3.__init__(self, lname)
		self.age = age
	
	def show_name(self):
		return f'{self.fname} {self.lname}'
orang = ChildClass4('jaka', 'prima', 30)
print("orang", orang.show_name())






#magic_method:
#__new__ = membuat new instance
#__init__
#terpanggil setelah instance terbuat oleh __new__(), tapi sebelum return ke caller. agit rgument yang ter passed ke class construtor expression. jika base class memiliki __init__() method, derived/diturunkan class __init__() method jika apapun harus explicitly/jelas terpanggil oleh proper inisialisasi dari base class part dari contoh, misal b = buku() akan error karena harus ada params jika ada set params di __init__()

#__str__
#terpanggil oleh str(object) dan built-in functions format() & print() untuk komputasi informal atau print string representasi dari object

#__len__
#__del__
class buku(object):
	def __init__(self, judul, penulis, halaman):
		print('buku init')
		self.judul = judul
		self.penulis = penulis
		self.halaman = halaman

	def __str__(self):
		return "judul: %s, penulis: %s, halaman: %s" %(self.judul, self.penulis, self.halaman)
	
	def __len__(self):
		return self.halaman
	
	def __del__(self):
		print('buku hilang')

b = buku(judul='judul buku', penulis='penulis buku', halaman=10)
str(b) #'judul: judul buku, penulis: penulis buku, halaman: halaman buku'
len(b) #10
del b # buku hilang dan manggil b.judul = undefined




# ------------------------------------------------------------------- ITERATORS
# object contains countable number of values
# iterator vs iterable
# list, tuple, dict, set iterable obj
# ex obj have a iter() method
tuple_data = (1,2,3,4)
iter_tuple_data = iter(tuple_data)
print("NEXT: ", next(iter_tuple_data))
print("NEXT: ", next(iter_tuple_data))
print("NEXT: ", next(iter_tuple_data))
print("NEXT: ", next(iter_tuple_data))

# create iterator
class IteratorClass:
	def __iter__(self):
		self.a = 1
		return self

	def __next__(self):
		if self.a <= 10:
			x = self.a
			self.a += 1
		else:
			raise StopIteration
		return x

iterator_class_instance = IteratorClass()
my_iter = iter(iterator_class_instance)
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
print("NEXT: ", next(my_iter))
# print("NEXT: ", next(my_iter))

# ------------------------------------------------------------------- POLYMORPHIS 
# dimana method dari class, memiliki method yang sama tapi bisa memanggil hal yang berbeda
# contoh anjing, kucing punya method yang sama suara() tapi hasilnya bisa berbeda




