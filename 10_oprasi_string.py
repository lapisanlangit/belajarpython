
# concate
nama_awal="Andi"
nama_tengah="P"
nama_akhir="Haholongan"

nama_lengkap=nama_awal+" "+nama_tengah+"'"+nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang=len(nama_lengkap)
print(panjang)

# cek apakah ada character tertentu dalam string
d="d"
status= d in nama_lengkap
print(status)
# not in
d="d"
status= d not in nama_lengkap
print(status)

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print(nama_lengkap[0])
print(nama_lengkap[1])
print(nama_lengkap[-1])
print(nama_lengkap[0:3]) #indek ke 0 - 2
print(nama_lengkap[1:4]) #index ke 1 -3
print(nama_lengkap[0:11:2]) #index ke 0,2,4,6,8
print(min(nama_lengkap)) #kode ascii paling kecil spasi
print(max(nama_lengkap)) #kode ascii paling besar

data="otong surotong"
print(data.count("o"))

salam="hallo Bro"
print("normal "+salam)
print("uppercase "+salam.upper())
print("lowercase "+salam.lower())

# pengecekan methode
nama="sisY"
print('cel lowercase '+str(nama.islower())) #bolean true false

judul="It is Okay not tobe Ok"
cek_judul=judul.istitle() #cek semua kata huruf besar depannya = boolean
print(cek_judul) 

# cek character depan belakang
alamat="alamatnya adalah depok".startswith("alamatnya")
print(alamat)
alamat="alamatnya adalah depok".endswith("depok")
print(alamat)


pisah=['aku','sayang','kamu']
gabung=' '.join(pisah)
print(gabung)
gabung=' - '.join(pisah)
print(gabung)
# dipisahkan
kalimat='aku-sayang-kamu'
print(kalimat.split('-'))

# rata kanan , kiri dan center = rjust(),ljust,center()
kanan="kanan".rjust(10)
print("'"+kanan+"'")

kiri="kiri".ljust(10)
print("'"+kiri+"'")

tengah="tengah".center(10,":")
print("'"+tengah+"'")
# menghilangkan
print(tengah.strip(":"))
