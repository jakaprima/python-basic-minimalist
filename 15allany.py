#memudahkan cek boolean yang match dalam perulangan. all() return True 

# sama dengan ini
# def all(perulangan):
# 	for element in perulangan:
# 		if not element:
# 			return False
# 	return True

list = [True,True,False,False]
any(l) # True
all(l) # False