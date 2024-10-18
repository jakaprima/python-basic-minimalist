# single and double quote
# quotes inside quotes
'spam eggs'  # 'spam eggs' single quotes
# ESCAPE CHARACTER
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
'doesn\'t'  # "doesn't" escape single quotes

# string to variable
a = "baris1\n baris2"  # new line
print(a)
# baris1
# baris2
print(r"C:\\files\name")  # print row dan ga jadi new line

# string beda" indent
# multiline strings
print("""\
bebas
	sdgasjdf
	 asdf
	 		afsdf
""")

# glued + repeat with * !behaviorjavascriptrepeat
3 * 'jaka' + 'prima'
# jakajakajakaprima

# gabung tanpa operator !behaviorjavascript
'jaka' 'prima'
# jakaprima

# output string array data !behaviorjavascript
# string are arrays
a = 'jako'
a[2]  # k
a[-1]  # o
a[1:3]  # ak string ambil dari index 1 dan ambil 3-1 = 2, ambil 2 data
a[:1] + a[3:]  # jo

# looping through a string
for data_loop in 'jaka':
    print("loop through string:", data_loop)

# string length
len(a);

# check string in
data_txt = "this is content need to exist search this: YESS aa"
print("YESS" in data_txt)
if "YESS" in data_txt:
    print("EXIST")
    
# check if not
if "NO TEXT" not in data_txt:
    print("EXIST")
    
# slicing strings
slicing_string = "Hello World"
print(slicing_string[2:5])
print(slicing_string[:5])
print(slicing_string[6:])
print(slicing_string[-5:-2]) # negative index

# modify string
modify_string = " Hello, World "
print(modify_string.upper())
print(modify_string.lower())
print(modify_string.strip()) # remove whitespace
print(modify_string.replace('H', 'J')) # replace string
print(modify_string.strip().split(',')) # split string

# F-String
age = 30
f_string = f"Jaka, {age}"
print(f_string)

price = 30
f_string = f"Price, {price:.2f}"
print(f_string)

# STRING METHODS
# capitalize()	Converts the first character to upper case
print("test".capitalize())
# casefold()	Converts string into lower case
print("Test".casefold())
# center()	Returns a centered string

# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning



# traverse
a = '123456789'
a[1::2]  # '2468'
a[0::2]  # '13579'
a[::-1]  # '987654321'
