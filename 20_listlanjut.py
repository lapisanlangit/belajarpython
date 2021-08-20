barang=['buku','meja','kursi']

print(barang)

barang.append('pensil')
print(barang)

barang.extend('dompet')
print(barang)


barang.insert(2,'sepeda')
print(barang)

jumlah=barang.count('sepeda')
print("jumlah sepeda adalah",jumlah)

#remove data
barang.remove('sepeda')
print(barang)

#copy list
stuff=barang.copy()
stuff.append('gelas')
print(stuff)


