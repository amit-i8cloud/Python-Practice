# File Handling

# with open('demo.txt','r') as file:

#   data = file.read();

#   print(data)

# file = open('demo.txt','r')

# d = file.read()

# print(d)

# file.close()

# read(),readline(),readlines()

# with open('demo.txt','r') as file:

#   line1 = file.readline()

#   line2 = file.readline()

#   line3 = file.readline()

#   line4 = file.readline()

#   print(line1.strip(),line2.strip(),line3.strip(),line4.strip())

# with open('demo.txt','r') as file:

#   lines = file.readlines()

#   print(lines)

#   for line in lines:

#     print(line.strip())

'''

Notes::

read() :

  -> reads the entire content in single string.

  -> use when length is smaller of the content

readline():

-> reads one line at a time .

-> good to use when we have large data as chunks

readlines():

-> reads all strings and stores in the list of strings.

'''
from logging import exception

# Writing to the file (if not found . creates a new file )

# write() -> To write a single string to the file

# writelines() -> write a lisy of strings to file

# write using 'w'

# with open('demo.txt', 'w') as file:

#   file.write('Xerox563 Added to Console !! \n')

#   file.write('Stealth Mode is Activated !! \n')

# fs = file.read()

# print(fs)

# write using 'a' -> used in logging system

# with open('demo.txt', 'a') as file:

#   file.write('\n Xerox563 Added to Console !! \n')

#   file.write('Stealth Mode is Activated !! \n')

# arr = ["Ferrari \n","BMW \n","Bugatti \n","Mustang GT \n"]

# with open('demos.txt', 'a') as file:

#  file.writelines(arr)

# File Cursor and seek()

# determines where in the file pyhton reads or writes to

'''

Default Behavior

When you open a file:

-> The cursor starts at position 0

-> After reading or writing, the cursor moves forward

Why Use seek()?

-> Re-read from the beginning without reopening the file

-> Skip or rewind to specific positions

file.tell() -> tells the cursor position

'''

# with open('demos.txt', 'r') as file:
#     print(file.read(5))
#
#     file.seek(0)
#
#     print('Cursor is at ::', file.tell())
#
#     print(file.read(5))
#
#     file.seek(0)
#
#     print('Cursor is at ::', file.tell())
#
#     print(file.read())

# with open('hack.txt','w') as fs:
#     fs.write("Hello from Metasploit !! \n")
#     fs.write("Metasploit is an payload creation linux based tool ")
#
# with open('hack.txt','r') as fs:
#     res = fs.readlines()
#     for line in res:
#         print(line.split())
#     print(res)

# with open('hack.txt','r') as fs:
#     print(fs.read(5))
#     fs.seek(6)
#     print(fs.read(5))
#     print("Cursor is at :: ",fs.tell())

'''
Note::
f = open("data.txt", "r")
content = f.read()
print(content)
f.close() 

If an error occurs before f.close(), the file may stay open → leads to:
Memory leaks
File locking issues
Data corruption
'''

# Binary files -> reading (rb) , writing (wb)
# with open("logo.png", "rb") as f:
#     image_bytes = f.read()
#     print(type(image_bytes))  # Output: <class 'bytes'>

# arr = [" Alex ","Bruno ","Mars "]
# with open('dextr.txt','a') as fs:
#     fs.writelines(arr)
    # r = fs.read()
    # print(r)
# with open("dextr.txt",'r+') as fs:
#     fs.write("Amanda ")
#     fs.seek(0)
#     print(fs.read())

'''
:: Error Handling !!
| Exception             | When It Happens                              |
| --------------------- | -------------------------------------------- |
| `FileNotFoundError`   | File does not exist when trying to open it   |
| `PermissionError`     | You don't have permission to access the file |
| `IsADirectoryError`   | You try to open a directory as a file        |
| `IOError` / `OSError` | General file input/output problems           |

'''
# try:
#     with open('dextrr.txt','r') as fs:
#         d = fs.readline()
#         print(d)
# except FileNotFoundError as e:
#     print("File Not Found !",e)
# except PermissionError as e:
#     print("Permisiion Error !",e)
# except IsADirectoryError as e:
#     print("Its not a Directory !",e)
# except exception as e:
#     print("Error Occured !",e)

'''
Modes in File Handling !! [9 Modes]
| Mode   | Meaning        | Description                                      |
| ------ | -------------- | ------------------------------------------------ |
| `'r'`  | Read           | Opens file for reading. File must exist.         |
| `'w'`  | Write          | Creates or overwrites file. Truncates if exists. |
| `'a'`  | Append         | Opens file for appending. Creates if not exist.  |
| `'r+'` | Read + Write   | Reads and writes. File must exist.               |
| `'w+'` | Write + Read   | Overwrites or creates. Truncates file if exists. |
| `'a+'` | Append + Read  | Appends and reads. Cursor starts at **end**.     |
| `'x'`  | Create         | Creates file. Fails if file exists.              |
| `'b'`  | Binary         | Used with other modes for binary files.          |
| `'t'`  | Text (default) | Default mode for text files.                     |

'''