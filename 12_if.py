nilai=75

if nilai==75:
    print("nilai anda ",nilai)

# tidak recommended karena nilai itu object
# if nilai is 75:
#     print("nilai anda",nilai)

if nilai >= 80:
    print("nilai bagus")
else:
    print("nilai jelek")


barang=["sate","gadogado","ayam goreng"]
beli="sate"

if beli in barang:
    print("ada")

if not beli in barang:
    print("tidak ada")