data_integer=1

print("data ini ",data_integer)
print("type data ",type(data_integer))


data_float=1.5

print("data ini ",data_float)
print("type data ",type(data_float))



data_string="jati"

print("data ini ",data_string)
print("type data ",type(data_string))


data_bool=True

print("data ini ",data_bool)
print("type data ",type(data_bool))

data_complex=complex(5,6)

print("data ini ",data_complex)
print("type data ",type(data_complex))

# dari bahasa c
from ctypes import c_double,c_char
data=c_double(10.5)
print("data ini ",data)
print("type data ",type(data))