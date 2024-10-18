# list python mengetahui senyawa tipe data, digunakan untuk grupin bersama dengan value lain. paling
# serbaguna/versatile adalah list, dimana dapat ditulis sebagai list dari pemisahan koma value (item) antara kurung
# persegi, list mungkin mengandung tipe data berbeda, tetapi biasanya semuanya tipe yang sama

# range menjadi list
print("range menjadi list")
list(range(4))  # output: [0, 1, 2, 3]

array = [1, 2, 3, 4]

# --------------------------------------------------------------------- ACCESS LIST ITEMS (GET)
thislist = ['a', 'b', 'c', 'd', 'e']
print("thislist", thislist[1])

# NEGATIVE INDEX
print("NEGATIVE", thislist[-1])

# RANGE OF INDEXES
print("RANGE OF INDEX", thislist[1:3])

# CHECK ITEM EXISTS
if "b" in thislist:
    print("yes b in list")

# LENGTH
print(len(array))

# LIST VALUE CAN BE ANY DATATYPE
list_data_type = ["abc", 34, True, 40, "male"]

# LIST CONSTRUCTOR
thislist = list(("apple", "banana"))

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# concatenate
print()
array + [5, 6, 7, 8, 9, 10]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ------------------------------------------------------------------------ CHANGE LIST ITEMS VALUE (UPDATE) 
# mutable (dapat diubah)
array2 = [2, 4, 8, 17]
array2[3] = 16
print(array2)  # [2, 4, 8, 16]

# CHANGE A RANGE OF ITEM VALUES
range_item_values = [1,2,3,4,5]
range_item_values[1:3] = [6,7]
print("CHANGE A RANGE OF ITEM VALUES", range_item_values)


# -------------------------------------------------------------------------------- ADD LIST ITEMS (CREATE) 
# insert on specific index
# INSERT ITEMS
array3 = [2, 4, 8]
array3.insert(1, 10)
print("ARRAY INSERT", array3)

# append / tambah data di akhir item
array3.append(2 ** 4)
array3  # [2, 4, 8, 16]


# EXTENDS
# append element from another list
output = []
array_extends1 = [1,[2,3],4,5,[6,7,10],11]
for data in array_extends1:
    if isinstance(data, list):
        output.extend(data)
    else:
        output.append(data)
print("EXTENDS:", output)

# ADD (tuples, sets, dictionaries etc.) to LIST
add_any = ['a', 'b', 'c']
tuples_data = ('d', 'e')
add_any.extend(tuples_data)
print("ADD ANY:", add_any)

# ------------------------------------------------------------------ REMOVE LIST ITEMS (DELETE) 
list_data_remove = ['a', 'b', 'c', 'd', 'e', 'f']
list_data_remove.remove('b')
print("REMOVE LIST ITEMS BY VALUE:", list_data_remove)

# REMOVE SPECIFIED INDEX WITH POP
list_data_remove.pop(1)
print("REMOVE LIST WITH POP", list_data_remove)

# REMOVE SPECIFIC INDEX WITH DEL
del list_data_remove[1]
print("REMOVE SPECIFIC INDEX WITH DEL", list_data_remove)

# CLEAR ALL LIST
list_data_remove.clear()
print("CLEAR ALL", list_data_remove)

# ------------------------------------------------------------------ LOOP LIST
# loop through a list
loop_data = [1,2,3,4,5,6,7,8]
for data in loop_data:
    print("loop:", data)

# loop throught index number
for data in range(len(loop_data)):
    print("LOOP BY RANGE:", data)

# while
i = 0
while i < len(loop_data):
    print("WHILE:", loop_data[i])
    i = i+1

# LOOPING USING LIST COMPREHENSION
thislist = ["apple", "banana", "cherry"]
new_list = [print(x) for x in thislist]

# -------------------------------------------------------------------------- LIST COMPREHENSION (shorter syntax create list)
# output = [data_return loop condition]
# iterable can be any iterable object, like a list, tuple, set etc.
# WITH STANDARD
list_comprehension = ['a', 'b', 'c', 'd', 'e']
# output = []
# for data in list_comprehension:
#     if 'a' in data:
#         output.append(data)
# print(output)

# WITH LIST COMPREHENSION
output = [data for data in list_comprehension if 'a' in data]
print("LIST COMPREHESSION: ", output)

# ['yaya', 'b', 'c', 'd', 'e']
# output = [(data if data != 'a') else "yaya" for data in list_comprehension]
output = [data if data != "a" else "yaya" for data in list_comprehension]
print("LIST COMPREHESSION: ", output)

# -------------------------------------------------------------------------------------- SORT LIST
# ALPHABET
array5 = ['a', 'c', 'b', 'd']
array5.sort()
print("SORT ALPHABET:", array5)  # [1, 2, 4, 4, 5, 6, 7]
# NUMERICALLY
array5 = [4, 2, 1, 5, 6, 7, 4]
array5.sort()
print("SORT NUMERIC:", array5)  # [1, 2, 4, 4, 5, 6, 7]
# SORT DESCENDING
array5.sort(reverse=True)
print("SORT DESCENDING:", array5)  # [7, 6, 5, 4, 4, 2, 1]
# CUSTOMIZE SORT
# Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23]
def func_customize_sort(n):
    return abs(n-50)
thislist.sort(key=func_customize_sort) # [50, 65, 23, 82, 100]
print("CUSTOMIZE SORT", thislist)
# Berikut langkah-langkah dari proses sorting ini:
# 50 most closed 50 (difference/selisih 0).
# 65 more close with 50 than 23 because (difference 15 for 65-50, while 23 has difference 27).
# 82 more far from 50 (difference 32).
# 100 is most far from 50 (difference 50).

# CASE SENSITIVE SORT
# error
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print("CASE SENSITIVE SORT UNEXPECTED RESULT: ", thislist)
# solved with
thislist.sort(key=str.lower)
print("CASE SENSITIVE SORT: ", thislist)

# REVERSE ORDER
array4 = [1, 2, 3, 4, 5, 6, 7, 8]
array4.reverse()
print(array4)  # [8, 7, 6, 2, 1]


# -------------------------------------------------------------------------------------------------------- COPY LIST
# with copy method
list_origin = [1,2,3,4,5]
list_copy = list_origin.copy()
list_copy[1] = 3
print("LIST ORIGIN", list_origin)
print("LIST COPY", list_copy)

list_origin = [1,2,3,4,5]
list_copy = list(list_origin)
list_copy[1] = 3
print("LIST ORIGIN", list_origin)
print("LIST COPY", list_copy)

# -------------------------------------------------------------------------------------------------------- JOIN LIST
# JOIN 2 LIST
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list_join = list1 + list2
print("LIST JOIN: ", list_join)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
for x in list2:
    list1.append(x)
print("LIST JOIN WITH APPEND: ", list1)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1.extend(list2)
print("LIST JOIN WITH EXTEND: ", list1)

# ----------------------------------------------------------------------------------------------------------------- LIST METHOD
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# slices / potong
array4 = [1, 2, 3, 4, 5, 6, 7, 8]
array4[2:5] = []  # dari index 2 5-2 = 3 hapus 3 data
array4  # [1, 2, 6, 7, 8]



l1 = [1, 2, 1, 2, 1]
l2 = [3, 4, 3, 4, 3]

array6 = [l1, l2]  # matrix
print(array6[0])
