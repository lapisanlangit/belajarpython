# enumerate
for i, nama in enumerate(makanan):
    print(i,nama)

# zip 
pegawai=["andi","bayu","ari","shayla"]

for peg,mak in zip(pegawai,makanan):
    print("Pegawai ",peg," suka makanan ",mak)

# pakai set 
nama_anak={"caca","bayu","ari"}
# sorted 
for i in sorted(nama_anak):
    print(i)

# pakai dictionary 
member={
    "nip":100,
    "nama":"jati",
    "alamat":"pati"
}

print("x" *30)
for i,v in member.items():
    print(i,v)