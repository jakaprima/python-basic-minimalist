# unchangeable, allowed duplicate, allow any type
tuple_data = ("data", 1, True, "data")
print("TYPE:", type(tuple_data))
# --------------------------------------------------------------- length
print("LENGTH:", len(tuple_data))
# ----------------------------------------------------------- tuple constructor
tuple_prepare = tuple(('a', 'b', 1, 2))
print("TYPE TUPLE CONSTRUCTOR:", type(tuple_prepare))

# --------------------------------------------------------------- ACESS TUPLE ITEMS
print(tuple_prepare[1])
print(tuple_prepare[-1])
print(tuple_data[1:3])
print(tuple_data[-1:-3])
if 1 in tuple_data:
    print("exists")
# ---------------------------------------------- UPDATE (unchangeable but cannot )
tuple_data = ("apple", "banana", "cherry")
tuple_data_to_list = list(tuple_data)
tuple_data_to_list[1] = "kiwi"
tuple_data = tuple(tuple_data_to_list)
print(tuple_data)

tuple_data_to_list = list(tuple_data)
tuple_data_to_list.append("append_data")
tuple_data = tuple(tuple_data_to_list)
# or
new_tuple_data = ('new_data',)
tuple_data += new_tuple_data
print("tuple_data", tuple_data)
# remove
tuple_data_to_list = list(tuple_data)
tuple_data_to_list.remove('new_data')
tuple_data = tuple(tuple_data_to_list)
print("tuple_data", tuple_data)
# clear
del tuple_data
# print("tuple_data", tuple_data) #this will raise an error because the tuple no longer exists
# -------------------------------------------------------------------------------- UNPACKING TUPLE
tuple_data = ("A", "B", "C", "D")
(a,b,c,d) = tuple_data
print("b", b)
# using asterisk *
tuple_data = (1,2,3,4,5,6,7,8,9,10)
(a,b,*c) = tuple_data
print("c", c)

# -------------------------------------------------------------------------------- LOOP
tuple_data = (1,2,3,4,5,6,7,8,9,10)
for x in tuple_data:
    print('x', x)
# loop through index
for x in range(len(tuple_data)):
    print("x1:", tuple_data[x])
# while loop
i = 0
while i < len(tuple_data):
    print("while:", tuple_data[i])
    i+=1
# -------------------------------------------------------------------------------- JOIN
tuple_data = (1,2,3,4)
tuple_data2 = (5,6,7,8)
tuple_data3 = tuple_data + tuple_data2
print("join:", tuple_data3)
# -------------------------------------------------------------------------------- MULTIPLY
tuple_data = (1,2,3,4)
tuple_data2 = tuple_data * 2
print("MULTIPLY:", tuple_data2)

# -------------------------------------------------------------------------------- METHODS
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
