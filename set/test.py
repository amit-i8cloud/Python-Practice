# sets are unordered, unchangeable,and unindexable
arr = {1, 2, 3, 4, 5, 67, 8, 1,52}
# print(arr)

# add
# arr.add(11)
# print(arr)

#update
# brr = [22,11,33,44,55,66]
# arr.update(brr)
# print(arr)
# print(type(arr))
# print(len(arr))

# remove,discard(If element does not exists , it doesnot gives the errors),pop() -> removes the random element from the set
# arr.discard(1)
# arr.remove(2)
# x = arr.pop()
# print(x)
# print(arr)

# Join Sets
brr = {2,3,4,5,6,7,2}
# arr.update(brr)
# print("Update Result ",arr)
# x = arr.union(brr)
# print("Union Result ",x)
# y = arr.difference(brr) or arr -brr  # It keeps items of first set that are not in the second set
# print("Difference Result ",y)
# z = arr.intersection((brr)) # It returns the common elements
# print("Intersecton Result ",z)

crr = {112,113,114,115,116,117,118,119}
op = arr | brr | crr
print("Result : " ,op)