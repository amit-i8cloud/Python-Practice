# List -> changeable duplicates
arr= [1,2,3,4,5,67,8,9]

#print
# print(arr)
# for i in range(0,len(arr)):
#     print(arr[i])
# arr[0] = 677 # changeable
#print(arr[-2]) # negative index
# print(arr[2:4]) # 2 -> 3
# print(arr[:4])
#
# # if item exists
# if 670 in arr:
#     print("Element exists !!")
#
# #insertion
# arr.insert(2,{
#     "name":"Raj",
#     "age":89
# })
# print(arr)
#
# #append
# arr.append(999);  # add element to the end
brr=["x","y","z"]
brr.extend(arr) #extend
# print(arr)
# print(brr)
#
# #removal
# brr.remove('z')
# brr.pop(0)
# print(brr)

#looping
# Way 1
# for i in brr:
#     print(i)

#Way 2
# for i in range(len(brr)):
#     print(brr[i])

# checking for element in the list
# t = False
# for i in range(0,len(brr)):
#     if brr[i] == 'zz':
#         t = True
#        # print("Z Found !!")
#
# if t == True:
#     print("Z Found !!")
# else:
#     print("Z not Found !!")


# x = int(input("Enter The Number !!"))
# # op : 1,4,9
# for i in range(1,x):
#     if i*i <= x:
#         print(i*i)
#     else:
#         break

# Join
x = [1,2,4,6,9]
y = [12,13,14,15,16]
# z = x + y  # Way1
for i in y:
  x.append(i)
print(x)

#copy
z =y.copy();
# z.sort()
z.sort(reverse=True)
print(z)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list