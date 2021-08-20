namaKucing="meme"

def ubahNama(nama):
    namaKucing=nama
    print("Nama Kucing baru adalah",namaKucing)


ubahNama('Meong') #variable jadi berubah di local saja
print("nama Kucing Awal",namaKucing)


# bisa diubah  menjadi global
namaKucing2="Nana"

def ubahNama2(nama):
    global namaKucing2
    namaKucing2=nama
    print("Nama Kucing baru adalah",namaKucing2)


ubahNama2('Maya') #variable jadi berubah di local saja
print("nama Kucing Awal",namaKucing2)

