#type
type(2) #int


#list
## append / tambah item di akhir list
a = [1,2,3,4,5]
a.append(6) #[1,2,3,4,5,6]

## extend / tambah semua item dalam list
b = [1,2]
c = [3,4]
b.extend(c) #[1,2,3,4]

#insert / tambah value pada spesifik index tertentu
d = [1,2,3]
d.insert(1, 10) # 1,10,2,3

#remove /hapus index yang berisi value
e = [1,2,3,4]
e.remove(3) # 1,2,4

#pop / hapus value pada spesifik index kalo ga ada index dihapus yang terakhir
f = [1,2,3,4]
f.pop(1) #1,3,4

#cek ada di index keberapa
g = [1,2,3,4]
g.index(3) #2

#cek ada berapa jumlah value yang sama
h = [1,2,3,4,4,4]
h.count(4) #3

#sort / mengurutkan
i = [1,3,2,3,5,6,8,6]
i.sort() # 1,2,3,3,5,6,6,8

#reverse / dibalik
j = [1,2,3,4,5]
j.reverse() #5,4,3,2,1

#list sebagai stack / LIFO pake append dan pop
#list seabagai queue / FIFO pake append dan popleft


# ------------------------ set -------------------------------#
# masukin dengan value yang unique value yang sama ga akan masuk
x = set()
x.add(1)
x.add(2)
x.add(1)
x # set([1,2])

#functional programming
##filter
def f(x): return x % 3 == 0 or x % 5 == 0
filter(f, range(2,25))
#[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]

##map
def f(x): return x*x*x
map(f, range(1, 11))
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


## reduce

## list comprehension // memahami list
#cara 1
a = []
for x in range(10):
	a.append(x**2)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#cara 2
a = [x**2 for x in range(10)]

#cara 3 jika ada if
a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]








