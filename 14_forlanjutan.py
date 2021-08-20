for i in range(0,10):
    print(i)

print('-'*10)
#dengan increment
for i in range(100,200,5):
    print(i)
print('-'*10)
# break
angka_dicari = 25

for i in range(0,40):
    print(i)
    if i is angka_dicari:
        print("angka ditemukan0",i)
        break