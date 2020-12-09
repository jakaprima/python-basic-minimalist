# list
# python mengetahui senyawa tipe data, digunakan untuk grupin bersama dengan value lain. paling serbaguna/versatile adalah list, dimana dapat ditulis sebagai list dari pemisahan koma value (item) antara kurung persegi, list mungkin mengandung tipe data berbeda, tetapi biasanya semuanya tipe yang sama

# range menjadi list
list(range(4)) #output: [0,1,2,3]

array = [1,2,3,4]

#concatenate
array + [5,6,7,8,9,10] #1,2,3,4,5,6,7,8,9,10

#mutable
array2 = [2,4,8,17]
array2[3] = 16
array2 #2,4,8,16

#append / tambah data di akhir item
array3 = [2,4,8]
array3.append(2**4)
array3 # 2,4,8,16

#slices / potong
array4 = [1,2,3,4,5,6,7,8]
array4[2:5] = [] #dari index 2 5-2 = 3 hapus 3 data
array4 # 1,2,6,7,8
array4.reverse()
print(array4) #[8, 7, 6, 2, 1]


array5 = [4,2,1,5,6,7,4]
array5.sort()
print(array5) #[1, 2, 4, 4, 5, 6, 7]

l1 = [1,2,1,2,1]
l2 = [3,4,3,4,3]

array6 = [l1,l2] #matrix
print(array6[0])





