# declarations
# s1 = 'Hellow World !!'
# s2 = "Hellow Amit !!"
# s3 = '''This is Amit from India
# I want to take my family to world every Part !!
#
# str = """Few Places include:
#  -> India
#  -> Japan
#  -> Switzerland
#  -> Norway
#  -> US
# """
from polib import text_type

str = "HelloWorld"
# print(s1)
# s3 = 'It\'s a sunny day'  # overwritten the previous string
# print(s1,s2,s3,s4)
# s5 = "Famous Cars All around the World !!\nBMW Black Series\nFord Mustand GT series\nFerrari\nPorsche"
# print(s5)
# s12 = "Unicode test: \u2764"
# print(s12)

"""
Notes ::
 -> Use "" when string contains '' , " Abck'brr' "
 -> Use '' when string contains "" . ' alex@"4321" ' 

"""
# # If both quotes appear in the string, use '\' escape characters
# s = "She said ,\"It's \"awesome!!\""
# print(s)
#
# # accessing the docstring(These are the literals that appear just after the definition of a function)
# def greet():
#     """This function just prints the greeting message
#      Welcome to My Project World !!
#      """
#     print("Hello Amit !! Good Evening !!")
#
# print(greet.__doc__) # accessing the doc string
# greet() # accessing the function by calling it



# Indexing
# for i in range(len(str)):
#     print(str[i])
#
# print("Length ",len(str))
# print(str[-1]) # prints the last character
# print(str[-2]) # print the last second charcter

#s Slicing
text = "PythonisaGoodProgrammingLanguage"
print(text[:2]) # from index o -> 1
print(text[2:]) # from index 2 -> end
print(text[-3:])  # last 3

print(text[0:20:2]) # from 0 -> 19 (sipping the 2nd charcter)

#reverse the string
print(text[::-1])
