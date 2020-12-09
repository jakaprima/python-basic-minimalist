# python 2 input
# python 3 input

x = 10
def jaka1():
	x = 20 #namespace variable
	return x
print(jaka1()) # 20
print(x) #10

x = 10
def jaka():
    global x
    x = 30
    return x
print(jaka()) #30
print(x) # 30


#if
x = int(input("masukkan inputan: ")) #input
if x < 10:
    print("x lebih kecil dari 10")
elif x == 3:
    print("x sama dengan 3")
else:
    print("yang lainnya")
# output x lebih kecil dari 10

#for
array1 = ['jaka', 'prima', 'maulana']
for x in array1:
	print(x, len(x))
#output
#jaka 4
#prima 5
#maulana 7

#insert di loop pada spesifik index
for w in array1[:]: #copy semua array untuk insert harus pake
	if len(w) > 5:
		array1.insert(0, w)
print(array1)
#output : maulana, jaka, prima, maulana


# range
print(range(5)) #0,1,2,3,4

#start from
print(range(6,10)) #6,7,8,9 10-6 = ambil 4 data

# range specify different increment (step)
range(0, 10, 3) # looping dengan increment +3 output: 0, 3, 9

range(-10, -100, -30) # looping dengan increment +(-30) output: -10, -40(-10+-30), -70(-40+-30)

# sum saat looping
sum(range(4)) # 0+1+2+3 output: 6

#loop with range
array1 = ['jaka', 'prima', 'maulana']
print(len(array1)) #3
for x in range(len(array1)):
	print(x, array1[x])
#output
#0 jaka
#1 prima
#2 maulana

#break statement (contoh: mencari factorial)
for x in range(2,10):
    for y in range(2, x):
        if x % y == 0:
            print(x, '=', y, '*', x/y)
            break
        else:
			# loop gagal tanpa menemukan factorial
            print(x, '')
# 3
# 4 = 2 * 2
# 5
# 5
# 5
# 6 = 2 * 3
# 7
# 7
# 7
# 7
# 7
# 8 = 2 * 4
# 9
# 9 = 3 * 3

#continue
for angka in range(1, 10):
    if angka % 2 == 0:
        print(angka, 'genap ditemukan')
        continue
    print(angka, 'angka ganjil')

# pass

# function
#fibonachi
def nameFunction(n): # menulis Fibonacci series ke n
	a,b = 0,1
	while a < n:
		print(a),
		a, b = b, a+b
nameFunction(2000)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


#default argument
def fungsi2(pesan, angka=4, pesan2='ya atau tidak!'):
	while True:
		ok = input(pesan)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no'):
			return False
		angka = angka - 1
		if angka < 0:
			raise IOError('error user')
		print(pesan2)

#fungsi2('apakah kamu ingin keluar?')
#fungsi2('apakah kamu ingin keluar?', 2)
#fungsi2('apakah kamu ingin keluar?', 2, 'pesankeluar')

#keyword argument

#arbitrary argument list / berubah"

#unpacking argument list with *
args = [3,6]
range(*args) # 3,4,5

#unpacking argument dictionaries with **
def f(arg1, arg2='default arg2 val', arg3='default arg3 val'):
	print(arg1)
	print(arg2)
	print(arg3)


dictionaries = {"arg1": "isi arg1", "arg2": "isi arg2", "arg3": "isi arg3"}

f(**dictionaries)

#lambda expression = anonymous func
def f(n):
	return lambda x: x + n
f2 = f(10)
print(f2(20)) # 30


func1 = lambda params: params+params
print(func1(10)) #20









