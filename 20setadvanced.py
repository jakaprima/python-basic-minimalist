s1 = set()
s1.add(1)
s1.add(2)
s1.add(1)
print(s1) #set([1, 2])
s1.clear() #set()



s2 = {1,2,3}
s2cp = s2.copy()
print(s2cp) #set([1, 2, 3])
s2.add(4)
s2.difference(s2cp) #set([4])


s31 = {1,2,3}
s32 = {1,4,5}
s31.difference_update(s32) 
print(s31) #{2,3}
s31.discard(2)
print(s31) #{3}

