#decorator dapat dipikir sebagai function dimana memodifikasi fungsionalitas ke function lain. dia membantu membuat code anda pendek dan pythonic

# def func():
# 	return 1

# #cek global dan local variabel yang ada
# s = 'ini adalah isi global variable'
# def func2():
# 	print locals() #buat cek isi local variable

# print globals().keys() #cek global variable


# def func3(nama='jaka'):
# 	print 'fungsi3 tereksekusi'
# 	def func4():
# 		print 'fungsi4 tereksekusi'
# 	def func5():
# 		print 'fungsi5 tereksekusi'
# 	if nama == 'jaka':
# 		print func5()
# 	else:
# 		print func4()
# print func3()





#reference kalo di javascript
def func6(func7):
	def func8():
		print 'exe func8'
	return func8
	print func7()

def func7():
	print 'exe func7'
func6(func7)


#decorator
def func8(func):
	def func9():
		print 'func9 exe'
		func()
		print 'exe setelah func10 terexe'
	return func9
# def func10():
# 	print 'fungsi10 ini butuh decorator'
# func11 = func8(func10)
# func11()


#@new_decorator // sama kaya atas hasilnya
@func8
def func10():
	print 'fungsi ini membutuhkan decorator'
func10()




