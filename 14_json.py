import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# conver to JSON with all type example:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# print(json.dumps(x))
# print(json.dumps(x, indent=4)) # for better read

# print("CHANGE DEFAULT SEPARATATOR", json.dumps(x, indent=4, separators=(". ", " = ")))
print("TO JSON WITH SORT", json.dumps(x, indent=4, sort_keys=True))