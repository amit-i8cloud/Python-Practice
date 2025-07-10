#  Tuples are ordered, immutable (unchangeable)[no updation , deletion and appendation], allows duplicate values ..
from itertools import count

arr = ("Apple","Ferrari","Dark","John the Ripper","HackTheBox","The Linux Foundation","Dark")
# print(arr)
# print(len(arr))
# print(type(arr))
# Accessing the Tuples is Possible
# To make changes in the data of the tuple first it needs to be converted to the list [append,remove,modification of element]
# temp = list(arr)
# for i in range(len(arr)):
#     temp[i] = temp[i] + ' :Hack'
#
# arr = tuple(temp)
# print(arr)

# Packing tuple -> When we create a tuple , normally we assign value to it this is packing
# unpacking -> extracting values [Destructing]
(x,*y,z) = arr
# print(x)
print(arr.count("Dark"))
# print(z)


# Methods
# count
# index
