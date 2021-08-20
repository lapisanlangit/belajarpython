class mahasiswa():
    nama=""
    nim=123
    __nilai=0 #private
    def __init__(self,input_nama,nim):
        self.nama=input_nama
        self.nim=nim
        
    def belajar(self):
        print(self.nama,' sedang belajar')
    def tambah(self,a,b):
        print(a+b)

        

# ucup=mahasiswa()
# print(ucup.nama)
# ucup.belajar()
# ucup.tambah(1,2)

ucup=mahasiswa("jati",234)
ucup.belajar()

# inheritance 
class Ojek():
    def __init__(self,nama,transmisi,daerah):
        self.nama=nama
        self.transmisi=transmisi
        self.daerah=daerah
    
    def cekIdMotor(self):
        print('nama',self.nama,'motor',self.transmisi,'daerah',self.daerah)


class Gojek(Ojek):
    pass

ojek1=Ojek('jati','manual','bandung')
ojek1.cekIdMotor()
ojek2=Gojek('bayu','otomatis','jakarta')
ojek2.cekIdMotor()
