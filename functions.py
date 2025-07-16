# from functools import reduce
#
# arr = [1, 2, 3, 4, 5, 6, 7, 89]
# # map
# def solve_map(n):
#     return n * 2
#
# t1 = map(solve_map, arr)
# print("Map obj:", t1)
# print("Output (Map):", list(t1))
#
#
# # filter
# def solve_filter(n):
#     return n % 2 == 1
#
# t2 = filter(solve_filter, arr)
# print('filter obj', t2)
# print('Output (filter):', list(t2))
#
#
# # reduce
# def add(a, b):
#     return a + b
#
# t3 = reduce(add, arr)
# print('Output (reduce):', t3)
from functools import reduce
from traceback import print_tb

# using lambda Functions
# its a tiny, one-line function with no name
# It's used when you need a quick, simple function without defining it using def.
# lambda arguments: expression

# def square(x):
#     return x*x
# print(square(2))

# square = lambda x:x*x
# print(square(3))
arr = [1,8,4,6,2,98,23,45,76,29]
# add = lambda x:x+x
# print(add(3))
str = ['alice','bob','dextrrr','xerox']
str.sort(key=lambda x:len(x))
print('After Sorting :',str)

ans = list(map(lambda y: y^2,arr))
print("After Appying map",ans)

ans_reduce = reduce(lambda x,y:x+y,arr)
print('Reduce Result :',ans_reduce)

