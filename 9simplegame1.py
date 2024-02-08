from random import shuffle

#kartu hati diamond, club dan spades
lambang_kartu_banyak = ('Hati','Diamond','Club','Spades')

#possible rank kartu
nomor_kartu_banyak = ( 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' )

#point value dictionaries
card_val = { 'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }

player1 = str(raw_input('masukkan nama player1? '))
player2 = str(raw_input('masukkan nama player2? '))

class Kartu():
	def __init__(self, lambang_kartu, nomor_kartu):
		print 'kartu diurutkan'

		

class Bandar():
	def __init__(self):
		print 'kocok kartu'
		self.semua_kartu = []
		for nomor_kartu in nomor_kartu_banyak:
			for lambang_kartu in lambang_kartu_banyak:
				self.semua_kartu.append(Kartu(lambang_kartu, nomor_kartu))
				# print lambang_kartu + nomor_kartu

Bandar()

kartuditanganplayer = []



import random

#boolean untuk mengetahui jika tangan sedang bermain
main = False

chip_pool = 100 #bisa juga pake raw input

bet = 1

restart_phrase = "pencet 'd' untuk deal dengan kartu lagi atau pencet 'q' untuk keluar "



#class untuk suit/cocok dan rank kartu
# class Kartu:
# 	def __init__(self, cocok, rank):
# 		self.cocok = cocok
# 		self.rank = rank

# 	def __str__(str):
# 		return self.cocok + self.rank

# 	def ambil_cocok(self):
# 		return self.cocok

# 	def ambil_rank(self):
# 		return self.rank

# class Tangan:
# 	def __init__(self):
# 		self.kartu_banyak = []
# 		self.value = 0
# 		self.ace = False

# 	def __str__(self):
# 		""" return string dari susunan tangan saat ini """
# 		susunan_tangan = ""

# 		#cara terbaik lakukan ini? pemahaman list
# 		for kartu in self.kartu_banyak:
# 			nama_kartu = kartu.__str__()
# 			susunan_tangan += "" + nama_kartu
# 		return 'tangan memiliki %s' %susunan_tangan

# 	def tambah_kartu(self, card):
# 		""" menambahkan kartu lain ke tangan """
# 		self.kartu_banyak.append(card)

# 		#cek untuk kartu ace
# 		if card.rank == 'A':
# 			self.ace = True 
# 		self.value += card_val[card.rank]

# 	def kalkulasi_val(self):
# 		""" kalkulasi value dalam tangan membuat aces dari 11 jika bust hand """
# 		if(self.ace == True and self.value < 12):
# 			return self.value + 10
# 		else:
# 			return self.value

# 	def draw(self,hidden):
# 		if hidden == True and main == True:
# 			#jangan perlihatkan kartu pertama yang tersembunyi
# 			memulai_kartu = 1
# 		else:
# 			memulai_kartu = 0
# 		for x in range(memulai_kartu, len(self.kartu_banyak)):
# 			self.kartu_banyak[x].draw()

# class Deck:
# 	def __init__(self):
# 		''' buat deck dalam order '''
# 		self.bungkus = []
# 		for cocok in cocok_banyak:
# 			for rank in ranking_banyak:
# 				self.bungkus.append(Kartu(cocok,rank))
# 	def kocok(self):
# 		""" shuffle/acak/kocok """
# 		random.shuffle(self.bungkus)



# 	def deal(self):
# 		''' ambil item pertama dalam deck '''
# 		kartu_satu = self.bungkus.pop()
# 		return kartu_satu

# 	def __str__(self):
# 		susunan_bungkus = ""
# 		for kartu in self.kartu_banyak:
# 			susunan_bungkus += " " + susunan_bungkus.__str__()
# 			return "didalam bungkus terdapat" + susunan_bungkus

# print('selamat datang di pertarungan kartu, mari mulai')

