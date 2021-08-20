a=4
b=2

hasil= a>b
print(hasil)

hasil= a<b
print(hasil)

hasil= a>=b
print(hasil)

hasil= a<=b
print(hasil)

c=4
hasil=c == 4
print(hasil)

c=4
hasil=c != 5
print(hasil)

# is adalah object identity
x=5
y=5

print ('nilai x =',x,'id : ',hex(id(x)))
print ('nilai y =',y,'id : ',hex(id(y)))

hasil = x is y
# hasil = x is 5 #kena warning karena bandingan object
# hasil = x == 5 #jadi mending pake ==

print(hasil)


