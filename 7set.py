# set are unordered, unchangeable, not allow duplicate
# access item only can from loop
set_data = {"a", 1, True}
# get the len
print("LEN:", len(set_data))
# set constructor
tuple_data = (1,2,3,4)
set_data = set(tuple_data)
print("SET CONSTRUCTOR:", set_data)
# ----------------------------------------------------------- ACCESS SET ITEMS, LOOP
for x in set_data:
    print("SET:", x)

# ----------------------------------------------------------- CHECK ITEM EXISTS
if 1 in set_data:
    print("EXISTS")
# ----------------------------------------------------------- ADD SET ITEMS
set_data.add('new_data')
print("new data", set_data)
# merge set
set_data = {1,2,3,4,5}
set_data2 = {6,7,8,9,10}
set_data.update(set_data2)
print("MERGE:", set_data)
# merge with list
set_data = {1,2,3,4}
list_data = [5,6,7,8]
set_data.update(list_data)
print("MERGE WITH LIST", set_data)
# ----------------------------------------------------------- REMOVE
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# thisset.remove("a") # will raise error
print(thisset)
# or 
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# thisset.discard("a") # will not raise error
print("DISCARD:",thisset)
# remove random
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("REMOVE POP:",x)
print("REMOVE POP:",thisset)
# clear all
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("CLEAR:",thisset)
# or
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # raise error
# ----------------------------------------------------------- JOIN
# join data unordered so will different order every execute
# use union, |, update, intersection, difference, symmetric difference, 
# join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("JOIN:",set3)
# or 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print("USE |:",set3)

# multiple join
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print("MULTI JOIN UNION:",myset)
# or 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print("MULTI JOIN USE | :",myset)

# join set & tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print("JOIN :",z)

# update, insert b to a
a = {"a", "b" , "c"}
b = {1, 2, 3}

a.update(b)
print("JOIN with UPDATE:",a)

# intersection (keep only duplicate)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print("INTERSECTION:", set3)
# or 
set3 = set1 & set2
print("INTERSECTION:", set3)

# intersection_update (keep only duplicate but will update original source too)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print("INTERSECTION UPDATE:", set1)

# difference (return set contain only item from first set that not present)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print("DIFFERENCE", set3)
# or 
set3 = set1 - set2
print("DIFFERENCE", set3)

# difference_update = (return set contain only item from first set but original source will change too)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print("DIFFERENCE UPDATE:", set1)

# symmetric difference (keep item that not present in both sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print("SYMMETRIC DIFFERENCE", set3)
# or 
set3 = set1 ^ set2
print("SYMMETRIC DIFFERENCE", set3)

# symmetric difference (keep item that not present in both sets)(original source will change too)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# method
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others