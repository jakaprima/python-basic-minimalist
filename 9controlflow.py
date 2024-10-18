# python 2 input
# python 3 input

# ----------------------------------------------------------------- SCOPE VARIABLES

# global scope
x = 10
def jaka1():
    # local scope
    x = 20  # namespace variable
    return x
print(jaka1())  # 20
print(x)  # 10

# GLOBAL KEYWORD
x = 10
def jaka():
    global x
    x = 30
    return x
print(jaka())  # 30
print(x)  # 30


# NON LOCAL KEYWORD
# make local scope var belongs to outer function
def func1():
    x = 'a'
    def func2():
        nonlocal x
        x = 'b'
    func2()
    return x
print("NON LOCAL KEYWORD:", func1())

# ----------------------------------------------------------------- IF ELSE
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
x = int(input("masukkan inputan: "))  # input
if x < 10:
    print("x lebih kecil dari 10")
elif x == 3:
    print("x sama dengan 3")
else:
    print("yang lainnya")
# output x lebih kecil dari 10

# short hand if else
a = 2
b = 330
print("A") if a > b else print("B")

# and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
# or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
# not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
# pass statement
if a > b:
    pass

# -----------------------------------------------------------------  WHILE LOOP
# while digunakan saat kita tidak tau pasti sampai atau berapa x looping yang kita inginkan
# akan gunakan ini selama kondisinya akan true
i = 1
while i < 6:
    print("WHILE LOOP:", i)
    i+=1

continue_loop = True
while continue_loop:
    answer = input('continue? y, yes, ye')
    if 'y' in answer:
        # continue_loop (to next iteration ignore execution after continue statement)
        continue
        print("WILL NOT SHOW")
    else:
        # we can use this
        break
        # or this:
        # continue_loop = False

# -----------------------------------------------------------------  FOR LOOP
array1 = ['jaka', 'prima', 'maulana']
for x in array1:
    print(x, len(x))
# output
# jaka 4
# prima 5
# maulana 7

# loop throught string
for x in 'jaka':
    print("LOOP THROUGHT STRING:", x)

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# insert di loop pada spesifik index
array2 = []
for w in array1[:]:  # copy semua array untuk insert harus pake
    print("w", w)
    if len(w) > 5:
        array2.insert(0, w)
print(array2)
# output : maulana, jaka, prima, maulana



# range
print(list(range(5)))  # [0,1,2,3,4]

# start from
print(range(6, 10))  # 6,7,8,9 10-6 = ambil 4 data

# range specify different increment (step)
range(0, 10, 3)  # looping dengan increment +3 output: 0, 3, 6, 9

range(-10, -100, -30)  # looping dengan increment +(-30) output: -10, -40(-10+-30), -70(-40+-30)

# sum saat looping
sum(range(4))  # 0+1+2+3 output: 6

# loop with range
array1 = ['jaka', 'prima', 'maulana']
print(len(array1))  # 3
for x in range(len(array1)):
    print(x, array1[x])
# output
# 0 jaka
# 1 prima
# 2 maulana

# break statement (contoh: mencari factorial)
for x in range(2, 10):
    for y in range(2, x):
        if x % y == 0:
            print(x, '=', y, '*', x / y)
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

# continue
for angka in range(1, 10):
    if angka % 2 == 0:
        print(angka, 'genap ditemukan')
        continue
    print(angka, 'angka ganjil')


# pass

# ---------------------------------------------------------------------------- FUNCTION
# fibonachi
# F(n)=F(n−1)+F(n−2)
# CONTOH
"""
F(n)=F(n−1)+F(n−2)
untuk n=0
F(0) = 0 (basis)
untuk n=1
F(1) = 1 (basis)
untuk n=2
F(2) = F(1) + F(0) = 1+0 = 1
untuk n=3
F(3) = F(2) + F(1) = 1 + 1 = 2
untuk n=4
F(4) - F(3) + F(2) = 2 + 1 = 3 
deret FIBONACCI = 0, 1, 1, 2, 3
"""
def nameFunction(n):
    # menulis Fibonacci series ke n
    a, b = 0, 1
    while a < n:
        print(f"{a}, {b}, a+b={a+b}"),
        a, b = b, a + b
        print(f"a={a} b={b}"),

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597


# default argument
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


# fungsi2('apakah kamu ingin keluar?')
# fungsi2('apakah kamu ingin keluar?', 2)
# fungsi2('apakah kamu ingin keluar?', 2, 'pesankeluar')

# keyword argument
def keyword_argument(data1, data2):
    print(data1, data2)
keyword_argument(data1=1, data2=2)

# arbitrary argument list / berubah"
# jika tidak tau berapa persis argument yang akan di masukan ke function buat seperti ini
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")


# arbitrary keyword argument (seperti arbitrary tapi argumentnya berbentuk key=value)
def my_function2(**kids):
  print("The youngest child is " + kids['fname'])
my_function2(fname="Emil", lname="Tobias")

# unpacking argument list with *
args = [3, 6]
range(*args)  # 3,4,5


# unpacking argument dictionaries with **
def f(arg1, arg2='default arg2 val', arg3='default arg3 val'):
    print(arg1)
    print(arg2)
    print(arg3)


dictionaries = {"arg1": "isi arg1", "arg2": "isi arg2", "arg3": "isi arg3"}
f(**dictionaries)

# passing list as argument
def passing_list_as_argument_example(data: list):
    print("data", data)
    for x in data:
        print("x", x)
passing_list_as_argument_example([1,2,3,4,5])

# only argument allowed (keyword argument not allowed)
def only_argument(data, /):
    print("ONLY ARG DATA:", data)
# only_argument(data='data') # TypeError: only_argument() got some positional-only arguments passed as keyword arguments: 'data'
only_argument('data')

# only keyword argument allowed
def only_keyword_argument(*, data):
    print("ONLY KWARGS DATA:", data)
# only_keyword_argument('data') # will error
only_keyword_argument(data='data')

# ------------------------------------------------------------------------------------------------- RECURSION
# defined function can call it self
def recursion_example(x):
    if (x > 0):
        result = x + recursion_example(x-1)
    else:
        result = 0
    return result

# recursion_example(1) mengembalikan 1 + 0 = 1.
# recursion_example(2) mengembalikan 2 + 1 = 3.
# recursion_example(3) mengembalikan 3 + 3 = 6.
# recursion_example(4) mengembalikan 4 + 6 = 10.
# recursion_example(5) mengembalikan 5 + 10 = 15.
# recursion_example(6) mengembalikan 6 + 15 = 21.
print("RECURSION:", recursion_example(6)) #21


# ------------------------------------------------------------------------------------------------------lambda (anonymous func)
# lambda arguments : expression
def f(n):
    return lambda x: x + n


f2 = f(10)
print(f2(20))  # 30

func1 = lambda params: params + params
print(func1(10))  # 20
