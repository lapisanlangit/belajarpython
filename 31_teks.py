# input output file 

# w:write
# r=read
# a=append
# r+=write and read

file=open("data.txt",'w')
file.write("contoh tulis file text")
file.write("\nbaris2")
file.write("\nbaris3")
file.close()

file2=open("data.txt",'r')
# print(file2.read())
print(file2.readline())
print(file2.readline())

# append 
file3=open('data.txt','a')
file3.write('\nbaris  4')
file3.close()



