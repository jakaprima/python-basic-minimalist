# bool represent two values True or False

# COMPARISON OPERATOR:
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

# LOGICAL OPERATOR
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

# IDENTITY OPERATOR
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y

# MEMBERSHIP OPERATORS
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# BITWISE OPERATORS
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2



print(10 > 9) # 10 greater than 9
print(10 == 9) # 10 same with 9
print(10 < 9) # 10 less then 9

# example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# evalute values
print(bool("Hello"))
print(bool(15))

# some values are False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# func return bool
def myFunction() :
  return True

print(myFunction())