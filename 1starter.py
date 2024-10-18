# install anaconda
# instal jupyter

"""
PYTHON INTERPRETER AND COMPILER
Sebuah "interpreter" (pengejaan bahasa Inggris: interpreter) adalah program komputer atau perangkat lunak yang digunakan untuk menjalankan kode sumber dalam bahasa pemrograman tertentu dengan cara menerjemahkannya ke dalam instruksi atau perintah yang dapat dimengerti oleh komputer atau sistem operasi. Interpreter berbeda dari kompiler, yang mengubah kode sumber menjadi kode mesin atau bahasa tingkat rendah sebelum menjalankannya.

Berikut adalah beberapa karakteristik utama dari interpreter:
Eksekusi Langsung: Interpreter mengeksekusi kode sumber secara baris per baris atau per pernyataan tanpa perlu menghasilkan kode mesin terlebih dahulu. Ini berarti pengembang dapat langsung melihat hasil eksekusi kode mereka tanpa harus menunggu proses kompilasi.
Proses Iteratif: Kode dalam bahasa pemrograman yang diinterpretasikan dapat dijalankan secara iteratif, memungkinkan pengembang untuk melakukan perubahan dan pengujian dengan cepat.
Lebih Lambat Dibandingkan Compiler: Interpreter biasanya lebih lambat dalam eksekusi kode daripada kompiler. Ini karena interpreter harus menerjemahkan kode sumber ke dalam instruksi setiap kali program dijalankan, sedangkan kompiler hanya perlu melakukan proses terjemahan sekali sebelum eksekusi.
Debugging yang Mudah: Interpreter sering kali menyediakan fitur debugging yang kuat, karena dapat memberikan pesan kesalahan yang lebih deskriptif dan memungkinkan pengembang untuk menjalankan kode baris demi baris atau dengan breakpoint.
Portabilitas: Kode yang dijalankan oleh interpreter sering lebih portabel, karena interpreter biasanya tersedia untuk berbagai platform dan sistem operasi. Ini memungkinkan program yang sama untuk dijalankan di berbagai lingkungan dengan sedikit atau tanpa modifikasi.
Contoh interpreter terkenal: Python, Ruby, Perl, dan JavaScript adalah contoh bahasa pemrograman yang menggunakan interpreter sebagai bagian dari eksekusi kode mereka.
Penting untuk diingat bahwa interpretasi dan kompilasi adalah dua pendekatan yang berbeda dalam menjalankan kode sumber, dan masing-masing memiliki kelebihan dan kelemahan sendiri. Keputusan untuk menggunakan interpreter atau kompiler tergantung pada kebutuhan dan tujuan pengembangan perangkat lunak yang sedang dilakukan.
"""

import sys
print(sys.version)

# basic: syntax, comments, variables
# casting spesifikasi tipe data dari variable
x = str(3)

# get type:
print(type(x))

# all datatype list
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# settings datatype
# x = "Hello World"	str
# x = 20	int
# x = 20.5	float
# x = 1j	complex
# x = ["apple", "banana", "cherry"]	list
# x = ("apple", "banana", "cherry")	tuple
# x = range(6)	range
# x = {"name" : "John", "age" : 36}	dict
# x = {"apple", "banana", "cherry"}	set
# x = frozenset({"apple", "banana", "cherry"})	frozenset
# x = True	bool
# x = b"Hello"	bytes
# x = bytearray(5)	bytearray
# x = memoryview(bytes(5))	memoryview
# x = None	NoneType


# legal variable name
myvar = "John"
my_var = "John" # snake case
_my_var = "John"
myVar = "John" # camel case
MYVAR = "John"
myvar2 = "John"
MyVar = "aa" # pascal case

# multiple value
x, y, z = 1, 2, 3
x, y, z = 1

# unpacking a collection
list_data = [1,2,3]
x, y, z = list_data


