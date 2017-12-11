# list
# python mengetahui senyawa tipe data, digunakan untuk grupin bersama dengan value lain. paling serbaguna/versatile adalah list, dimana dapat ditulis sebagai list dari pemisahan koma value (item) antara kurung persegi, list mungkin mengandung tipe data berbeda, tetapi biasanya semuanya tipe yang sama

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
array4[2:5] = [] #from index 2 5-2 = 3 remove 3 data
array4 # 1,2,6,7,8





