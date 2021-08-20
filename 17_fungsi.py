def tampil():
    print("tampil data")


tampil()

def harga(kg):
    harga=1000
    print("harganya ",harga * kg)

harga(20)

def guru(nama,pelajaran):
    print("nama guru",nama)
    print("mengajar",pelajaran)

# setting paramter bisa dibalik
guru(pelajaran="Fisika",nama="andi")

# paramateter dengan nilai default
def penjagaSekolah(nama,shift="siang"):
    print("Nama Penjanga Sekolah",nama)
    print("Shiftnya adalah",shift)

penjagaSekolah("Andi")
penjagaSekolah("Maman","malam")

# return Value
def hasilHitung(a,b):
    return a+b


a=hasilHitung(1,2)
print(a)

# return multiple
def hasilHitung(a,b):
    hasilTambah=a+b
    hasilKurang=a-b
    return [hasilTambah,hasilKurang]

b=hasilHitung(10,3)
print(b)

# fungsi di dalam fungsi dalam bentuk parameter
def tambah(a,b):
    total=a+b
    return total

def total(tambahan,fungsilain):
    hasilnya=tambahan * fungsilain
    return hasilnya
b=total(3,tambah(1,2))
print(b)