## Dictionary Methods
person = {
    "name":"Alice",
}
# 1. get(key, default)
person = {"name": "Alice"}
print(person.get("name"))         # 'Alice'
print(person.get("age"))          # 30
print(person.get("age", 18))      # 18 (if i think age is not present in the person)

# 2. keys()
print(person.keys())               # dict_keys(['name'])

# 3. values()
print(person.values())            # dict_values(['Alice'])

# 4. items()
for key, value in person.items():
    print(key, value)

# 5. update()
person.update({"age": 25, "city": "NYC"})
print(person)

# 6. pop(key, default)
age = person.pop("age")            # ➝ 25
print(age)
print(person)

# 7. popitem()
last_item = person.popitem()      # ➝ ('city', 'NYC')
print(last_item)

# 8. clear()
person.clear()
print(person)                      # {}

# 9. copy()
original = {"x": 10}
clone = original.copy()
print(clone)

# 10. setdefault()
user = {"id": 101}
user.setdefault("name", "Guest")  # adds 'name' if missing
print(user)

# 11. fromkeys()
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)                # {'a': 0, 'b': 0, 'c': 0}

# Check if Key Exists
if "name" in user:
    print("Key exists")

# Looping through dictionary
for k in user:
    print(k, user[k])

for k, v in user.items():
    print(f"{k} = {v}")

# Merging dictionaries (Python 3.9+)
d1 = {'a': 1}
d2 = {'b': 2}
merged = d1 | d2
print(merged)
