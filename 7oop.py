#object oriented programming
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
	kategori = 'orang' # class variable yang dishare semua instances/contoh

	def __init__(self, argument):
		self.method = argument # instance variable unique to each instance
jaka = orang('jaka prima')
jaka.method # jaka prima
jaka.kategori # orang

#method
class lingkaran(object):
	pi = 3.14
	def __init__(self, radius=1):
		self.radius = radius
	def area(self):
		return (self.radius**2) * lingkaran.pi
	def set_radius(self, radius_baru):
		self.radius = radius_baru
	def get_radius(self):
		return self.radius
c = lingkaran(radius = 10)
c.area() #314.0
c.radius # 10
c.set_radius(20) 
c.radius # 20
c.get_radius() #10


#inheritence / hak waris
class orang(object):
	def __init__(self):
		print 'orang'
	def siapa(self):
		print 'nama'
	def aksi(self):
		print 'jalan'
class bayi(orang):
	def __init__(self):
		orang.__init__(self)
		print 'saya bayi'
	def siapa(self):
		print 'jaka'
	def aksi2(self):
		print 'minum'


d = bayi()
d # orang, saya bayi
d.siapa #jaka
d.aksi #jalan
d.aksi2 #minum


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
		print "buku dibuat"
		self.judul = judul
		self.penulis = penulis
		self.halaman = halaman
	def __str__(self):
		return "judul: %s, penulis: %s, halaman: %s" %(self.judul, self.penulis, self.halaman)
	def __len__(self):
		return self.halaman
	def __del__(self):
		print 'buku hilang'

b = buku(judul='judul buku', penulis='penulis buku', halaman=10)
str(b) #'judul: judul buku, penulis: penulis buku, halaman: halaman buku'
len(b) #10
del b # buku hilang dan manggil b.judul = undefined








