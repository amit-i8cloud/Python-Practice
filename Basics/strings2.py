# Helper Functions
# 1. strip()
# It is used to remove whitespaces(or other characters) , from the beginning  and end of the string .

# text = '   hello world   '
# print(text.strip())
#
# text = '\n\t Python\t\n'
# print(text.lstrip())  # removes the whitespaces from only left end
# print(text.rstrip())  # removes the whitespaces from only right end
# print(text.strip())   # removes the whitespaces from both the end
#
# text = "....hello...."
# print(text.strip("."))       # 'hello'
#
# name = "**Alice***"
# print(name.strip("*"))       # 'Alice'
#nnnnnnnnnnn
# combo = "-=Hello=-"
# print(combo.strip("-="))     # 'Hello'

# Note
# s = "abcHellmoabcabccc"
# print(s.strip("abc"))  # 'Hello' (removes all 'a', 'b', or 'c' from both ends)
#
# str = "abcdeFF"
#
# print(str.lower())
# print(str.upper())
# print(str.capitalize()) # first letter of string becomes capital
# print(str.title()) # each word ko capitalize kr deta hai
'''
------------------------------------------------------------------
#2. string searching  find(),index()
# it helps us to locate substrings inside a string
# returns the first occurance of the  substring in the string

 find() -> if substring not found , returns -1
 index() -> if string not found , returns teh valueEroor
'''
from pydoc import replace

# text = 'Hellow World !!'
# x = text.find('e')
# y = text.find('World')
# z = text.find("e",1)
# w = text.find('w',2,7)
# print(x,y,z,w)

# replace(old,new,count)

# text = 'orange apple orange mango'
# x = text.replace("orange","apple")
# print(text,x) # it does not chnage the original string
#
# y = text.replace('orange','papaya',1)
# print(y)
#
# # split(),join()
#
# s = "apple,banana,mango"
# parts = s.split('-')
# print(parts)
#
# t = "-".join(parts)
# print(t)

# text = "one two three four five "
# x = text.split(',',2)
# print(x)
# escape characters
'''
\n -> New Line
\t -> space
\' -> allows ' in the strings

'''