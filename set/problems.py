# sum of all elements of array
from ctypes import string_at

arr = [1,2,3,48,7,65,43]
# summ = 0
# for i in range(len(arr)):
#     summ += arr[i]
# print(summ)
#
# # largest element
# max_ans = -1e9
# for i in range(len(arr)):
#     max_ans = max(max_ans,arr[i])
# print(max_ans)

# reverse list
# arr = [10, 20, 30, 40, 50]

# # Reversing using a loop
# n = len(arr)
# for i in range(n // 2):
#     arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
#
# print("Reversed list:", arr)

# using two pointer
# s = 0
# e = len(arr) - 1
# while s < e:
#     arr[s],arr[e] = arr[e],arr[s] # swapping (a,b = b,a)
#     s+=1
#     e-=1
# print(arr)

#using reversed
# temp = []
# for val in reversed(arr):
#     temp.append(val)
# print(temp)
#
# arr = [1,2,3,4,5]
# # reverse loop
# for i in range(len(arr)-1,-1,-1):   # start from len(arr-1) , end before -1 , -1 each time loop works
#     print(arr[i])

 # count Occurances of x if present
arr = [1, 2, 2, 3, 4, 2]
x = int(input("Enter value of x: "))
ans = 0
# print("Ans: ",arr.count(x))
for i in range(len(arr)):
    if arr[i] == x:
        ans += 1

print("Count of", x, "is:", ans)

#count(arr.count(x) -> gives count of occurances of this element(x)

# Rotate List to the Right by k Steps

#
# arr = [1, 2, 3, 4, 5]
# k = 2
#
# # Normalize k to handle cases when k > len(arr)
# k = k % len(arr)
# rotated = arr[-k:] + arr[:-k]
# print("1. Rotated List:", rotated)

# Problem 2: Check if Two Lists are Anagrams
a = [1, 2, 3, 4]
b = [4, 3, 2, 1]

# Sort both and compare
if sorted(a) == sorted(b):
    print("2. Lists are anagrams")
else:
    print("2. Lists are not anagrams")

# Find Second Largest Element

arr = [5, 1, 9, 6, 9]

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print("3. Second Largest Element:", second)

#Find All Pairs with a Given Sum
arr = [1, 2, 3, 4, 5]
target = 6

print("4. Pairs with sum", target, ":")
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"   Pair: ({arr[i]}, {arr[j]})")

# Problem 5: Separate Positive and Negat.. Numbers

arr = [1, -2, 3, -4, 5, -6]

pos = []
neg = []

for num in arr:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print(" Posive Numbers:", pos)
print("Negative Numbers:", neg)
