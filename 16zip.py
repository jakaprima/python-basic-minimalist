#menggabungkan element dari dari setiap index dari list 1 dan 2
x = [1,2,3]
y = [4,5,6]

zip1 = zip(x, y) # [(1,4),(2,5),(3,6)]
zip2 = zip1[0] # (1,4)

a = [1,2,3,4,5]
b = [2,2,10,1,1]

for pasangan in zip(a,b):
	print max(pasangan) #2,2,10,4,5
	# print ('pasangan', pasangan)

# alur
# ('pasangan', (1, 2)) 
# 2
# ('pasangan', (2, 2))
# 2
# ('pasangan', (3, 10))
# 10
# ('pasangan', (4, 1))
# 4
# ('pasangan', (5, 1))
# 5

pake_map = map(lambda pasangan: max(pasangan), zip(a,b))
print pake_map #[2,2,10,4,5]

#object
o1 = {'a':1,'b':2}
o2 = {'c':3,'d':4}
zip3 = zip(o1,o2)
print zip3 #[('a', 'c'),('b','d')]

#itervalues
zip4 = zip(o2,o1.itervalues())
print zip4 #[('c',1),('d',2)]

def function1(o1,o2):
	object1 = {}

	for d1key, d2val in zip(o1,o2.itervalues()):
		object1[d1key] = d2val

	return object1

test = function1(o1,o2)
print test



