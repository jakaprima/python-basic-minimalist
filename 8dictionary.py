# dictionary (kamus) key: value pairs
# changeable, not allow duplicate
thisdict = {
  "year": 1964,
  "brand": "Ford",
  "model": "Mustang",
}
print("thisdict", thisdict)


# duplicate not allowed example:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("YEAR NOT DUPLICATE:", thisdict)

# Dictionary Item, Accessing Items (GET)
print("ACCESS DICT:", thisdict['brand'])

# length
print("LENGTH", len(thisdict))

# values can be any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# type
print("type", type(thisdict))

# dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print("dic constructor:", thisdict)

# ----------------------------------------------------------------------------------- ACCESS ITEMS (GET)
thisdict = {
  "year": 1964,
  "brand": "Ford",
  "model": "Mustang",
}
print("thisdict", thisdict['brand'])

# GET ALL KEYS as list
print(thisdict.keys())

# GET ALL VALUES as list
print(thisdict.values())

# get a list of the key:value pairs (as tuples in a list)
print(thisdict.items())

# check if key exists
if "brand" in thisdict:
    print("yes brand key exist in thisdict")

# --------------------------------------------------------------------------- CHANGE DICTIONARY ITEMS (UPDATE)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict["year"] = 2018
# or
thisdict.update({"year": 2018})
# ------------------------------------------------------------------------------ ADD ITEM (CREATE)
# add new key:value
thisdict['color'] = 'red'
# or
# thisdict.update({'color': 'red'})
# ------------------------------------------------------------------------------ REMOVE ITEM (DELETE)
# remove item by key
# thisdict.pop('model')
# del thisdict

# remove item last item
# thisdict.popitem()

# clear all to {}
# thisdict.clear()

# ------------------------------------------------------------------------------ LOOP DICT
for key in thisdict:
    print("key: ", key)
# or 
for key in thisdict.keys():
    print("KEY: ", key)


for key in thisdict:
    print("value: ", thisdict[key])
# or 
for value in thisdict.values():
    print("value: ", value)

# key value pairs
for key, value in thisdict.items():
    print(f"key: {key} value: {value}")

# ------------------------------------------------------------------------------ COPY DICTIONARY
# different copy_dict = this_dict with copy_dict = this_dict.copy() its allocated to different memory or reference so when this_dict update will not update copy_dict
copy_dict = thisdict.copy()
print("COPY DICT", copy_dict)

# ------------------------------------------------------------------------------ NESTED DICTIONARY
nested_dict = {
    'key': {
        "key2": value
    }
}
# access
print("NESTED:", nested_dict['key']['key2'])
# loop throght nested
for key, value in nested_dict.items():
    if isinstance(value, dict):
        for key2, value2 in value.items():
            print(f"key2:{key2} value2:{value2}")

# dictionary methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary



