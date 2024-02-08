# Tugas:
# berikan(
# 	makanan harga (harga dasar dari makanan), 
# 	tip percent (persentasi dari harga makanan sebagai tip)
# 	tax percent (persentase dari dari harga makanan yang ditambah sebagai pajak) dari makanan
# )

# cari dan print makanan total biaya

# catatan: yakin bahwa gunakan precise/ketepatan values untuk kalkulasi atau atau akan berakhir dengan hasil yang salah


# Input format
# baris pertama sebagai double (harga makanan sebelum tax dan tip)
# baris kedua sebagai integer (persentasi sebagai tip)
# baris ketiga sebagai integer (persentasi sebagai tax)

# Output Format
# output print total harga makanan adalah total harga dollar.
# dimana hasil perputaran dari seluruh biaya dengan menambahkan tax dan tip 

# Sample Input
# 12.00
# 20
# 8

# Sample Output
# total harga adalah 15 dollars.


import sys

if __name__ == "__main__":
    harga_makanan = float(input().strip())
    tip_persen = int(input().strip())
    pajak_persen = int(input().strip())
    
    tip = harga_makanan * tip_persen / 100
    tax = harga_makanan * pajak_persen / 100
    
    totalHarga = harga_makanan + tip + tax
    totalHargaBulat = round(totalHarga) 
    print('harga makanan = ', harga_makanan)
    print('tip =', tip)
    print('pajak = ', tax)
    print("harga total adalah = %i." % (totalHargaBulat)), 

