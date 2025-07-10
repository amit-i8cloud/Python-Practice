# 1. Find the Key with Maximum Value
# scores = {'Alice': 88, 'Bob': 95, 'Charlie': 90}
# t = 0
# t_t = ''
# for key,value in scores.items():
#     # t = max(t,value)
#     if value > t:
#         t = value
#         t_t = key
# print(t_t,t)


# 2. Group People by Age
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30}
]

group = {}
for x in people:
    age = x["age"]
    name = x["name"]
    if age not in group:
        group[age] = []
    group[age].append(name)

print(group)



# 3. Count Word Frequency (Ignore Case & Punctuation)
import string
text = "Hello, hello! How are you?"
text = text.lower()
for p in string.punctuation:
    text = text.replace(p, "")
word_freq = {}
for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print(word_freq)

# 4. Filter Dictionary by Condition
grades = {'math': 95, 'english': 65, 'science': 88}
filtered = {subject: score for subject, score in grades.items() if score > 70}
print(filtered)

# 5. Create Inverted Index
items = [
    {"item": "apple", "category": "fruit"},
    {"item": "carrot", "category": "vegetable"},
    {"item": "banana", "category": "fruit"}
]
index = {}
for entry in items:
    cat = entry["category"]
    item = entry["item"]
    index.setdefault(cat, []).append(item)
print(index)

# 6. Digit Frequency in Number List
numbers = [12, 34, 22]
digit_count = {}
for number in numbers:
    for digit in str(number):
        digit = int(digit)
        digit_count[digit] = digit_count.get(digit, 0) + 1
print(digit_count)
