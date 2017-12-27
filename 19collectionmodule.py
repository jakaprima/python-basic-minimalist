#collection module adalah build-in module yang mengimplementasikan spesial container datatypes melayani alternative ke python umum tujuan built-in contianers. 

#-------------------Counter-----------------------#
# counter adalah dict subclass dimana membantu count hashable objects yang tersimpan sebagai value
# ----------------------------------------- counter list
from collections import Counter
l = [1,2,2,2,2,2,3,3,3,4,1,2,1,12,3,32,1]
lCounter = Counter(l)
print(lCounter) #Counter({2: 6, 1: 4, 3: 4, 32: 1, 4: 1, 12: 1})

# ----------------------------------------- counter string
string = 'jaka'
sCounter = Counter(string)
print(sCounter) #({'a': 2, 'k': 1, 'j': 1})

# ----------------------------------------- counter word
kata = 'halo nama jaka halo'
katasplit = kata.split() #['halo', 'nama', 'jaka', 'halo']
kataCounter = Counter(katasplit)
print(kataCounter) #Counter({'halo': 2, 'nama': 1, 'jaka': 1})
ambildata = kataCounter.most_common(2) #ambil data
print(ambildata) #[('halo', 2), ('nama', 1)]


#------------------- Defaultdict -----------------------#
# adalah dictionary seperti objects dimana melayani semua method yang dilayani oleh dictionary tetapi mendapatkan argument pertama (default_factory) sebagai default tipe data untuk dictionary. gunakan defaultdict cara cepat untuk melakukan sama dic.set_default method


from collections import defaultdict
d1 = {'k1':1}
d1['k1'] #1
# d1['k2'] #keyError

d2 = defaultdict(object)
d2['satu']
d2['dua']
for x in d2:
	print x #dua satu










