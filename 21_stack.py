from collections import deque
tumpukan=[1,2,3,4,5,6]

# menghilangkan isi ist terahir
out=tumpukan.pop()
print("data keluar ",out)
print(tumpukan)

# queing
antrian=deque([1,2,3,4,5])
print ("data ",antrian)


antrian.append(6)
print ("masuk 6")
print ("data ",antrian)

antrian.append(7)
print ("masuk 7")
print ("data ",antrian)

out=antrian.popleft()
print ("keluar",out)
print ("data ",antrian)

