data=[1,2,3,4,5,6,7] 

# index dimulai dari 0
subdata=data[0]
print(subdata)

subdata=data[-3] #dari kanan
print(subdata)

subdata=data[0:4]  #index 0 sampai sebelum 4
print(subdata)

subdata=data[2:4]  #index 2 sampai sebelum 4
print(subdata)

print("-"*100)
subdata=data[:4]  #ambil semua sebelum index 4
print(subdata)

data2=[100,200,300,400]

cetak=data+data2
print(cetak)

print("-"*100)
# merubah content
data[2]=100
print(data)

databaru=data
databaru[3]=355
print("-"*100)
print(data) #maka content data ikut berubah walupun yang dirubah adalah databaru
# agar tidak tercopy maka ditambah seperti ini
databaru=data[:]
databaru[3]=455


# merubah content dengan slicing
print("-"*100)
data[1:3]=[100,200]
print(data)

# list dalam list
gabung=[data,data2]
print(gabung)
# akses content
b=gabung[0][2]
print(b)

# tambah data list
data.append(8)
print(data)

# panjang list
print(len(data))
