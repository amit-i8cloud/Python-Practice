import json

'''
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

data = [
    ["Alex",23,"CSE"],
    ["Arjit",21,"CS + AI"],
    ["Dextrr",25,"IT"]
]

with open("data.csv", 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

    file.flush()  # ✅ Ensure written data is flushed (all writes are flushed or written in the )
    file.seek(0)

    reader = csv.reader(file)
    for row in reader:
        print(row)
# ✅ flush() -> All writes are flushed from the buffer to the disk.
'''

# with open('db.json', 'r') as file:
#     data = json.load(file)
#     print(data)
#
# print(data["name"])

data = {
  "name": 'Mr. Robot',
  "age": '23',
  "specialization" : 'MetaSploit and Beef Frameworks',
  "Country": 'Anonymous',
  "Tools": 'Linux ,'
}

try:
  with open("db.json",'a') as file:
    json.dump(data,file,indent=3)
    print("File Written Successfully !!")

except FileNotFoundError as error:
    print("Error: ",error)
