# ## Dictionary Methods
# person = {
#     "name":"Alice",
# }
# # 1. get(key, default)
# person = {"name": "Alice"}
# print(person.get("name"))         # 'Alice'
# print(person.get("age"))          # 30
# print(person.get("age", 18))      # 18 (if i think age is not present in the person)
#
# # 2. keys()
# print(person.keys())               # dict_keys(['name'])
#
# # 3. values()
# print(person.values())            # dict_values(['Alice'])
#
# # 4. items()
# for key, value in person.items():
#     print(key, value)
#
# # 5. update()
# person.update({"age": 25, "city": "NYC"})
# print(person)
#
# # 6. pop(key, default)
# age = person.pop("age")            # ➝ 25
# print(age)
# print(person)
#
# # 7. popitem()
# last_item = person.popitem()      # ➝ ('city', 'NYC')
# print(last_item)
#
# # 8. clear()
# person.clear()
# print(person)                      # {}
#
# # 9. copy()
# original = {"x": 10}
# clone = original.copy()
# print(clone)
#
# # 10. setdefault()
# user = {"id": 101}
# user.setdefault("name", "Guest")  # adds 'name' if missing
# print(user)
#
# # 11. fromkeys()
# keys = ["a", "b", "c"]
# default_dict = dict.fromkeys(keys, 0)
# print(default_dict)                # {'a': 0, 'b': 0, 'c': 0}
#
# # Check if Key Exists
# if "name" in user:
#     print("Key exists")
#
# # Looping through dictionary
# for k in user:
#     print(k, user[k])
#
# for k, v in user.items():
#     print(f"{k} = {v}")
#
# # Merging dictionaries (Python 3.9+)
# d1 = {'a': 1}
# d2 = {'b': 2}
# merged = d1 | d2
# print(merged)

# List Methods & Techniques Cheat Sheet

# append() - Adds an element at the end of the list
arr = [1, 2, 3]
arr.append(4)
print(arr)  # [1, 2, 3, 4]

# insert() - Inserts element at specific position
arr.insert(1, 10)
print(arr)  # [1, 10, 2, 3, 4]

# extend() - Adds elements of another list
arr.extend([5, 6])
print(arr)  # [1, 10, 2, 3, 4, 5, 6]

# pop() - Removes and returns last item (or by index)
arr.pop()        # removes 6
arr.pop(1)       # removes 10
print(arr)

# remove() - Removes first occurrence of value
arr.remove(2)
print(arr)       # [1, 3, 4, 5]

# index() - Returns index of first occurrence
print(arr.index(3))  # 1

# count() - Counts occurrences of element
print(arr.count(4))  # 1

# sort() - Sorts the list in-place
arr.sort()
print(arr)       # [1, 3, 4, 5]

# reverse() - Reverses list in-place
arr.reverse()
print(arr)       # [5, 4, 3, 1]

# copy() - Returns shallow copy of list
copy_arr = arr.copy()
print(copy_arr)

# clear() - Removes all elements
copy_arr.clear()
print(copy_arr)  # []

# slicing - Gets sublist (start:stop[:step])
slice_arr = arr[1:3]  # [4, 3]
print(slice_arr)

# list comprehension
squares = [x * x for x in range(5)]
print(squares)   # [0, 1, 4, 9, 16]

# len() - Length of list
print(len(arr))

# max() / min()
print(max(arr))  # 5
print(min(arr))  # 1

# sum() - Sum of list
print(sum(arr))  # 13

# in - Check membership
print(3 in arr)  # True

# zip() - Combine two lists
names = ['a', 'b']
ages = [10, 20]
print(list(zip(names, ages)))  # [('a', 10), ('b', 20)]

