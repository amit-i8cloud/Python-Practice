# OOP -It's a style of programming where everything is built around objects and classes.
# class -> blueprint for object
# object -> real entity created using the class
# Attribute -> variable inside the class
# Method -> function inside the creation
# __init__ -> special method  that runs on
# s1 = Student(...) -> creates an object.

# Without Constructor
class Hello:
    def say_Hello(self):
        print("Hello !! Welcome to OOps !!")

x = Hello()
x.say_Hello()
# With Constructor
# class Car:
#     # Constructor
#     def __init__(self,arg1,arg2):
#         # these below values fills the object created
#         self.arg1 = arg1
#         self.arg2 = arg2
#     # method
#     def show_Details(self):
#         print(f"Car Brand : {self.arg1}, Car Model : {self.arg2} ")
#
#
# #object creation
# c1 = Car("Toyota","Red")
# c2 = Car("Ford Mustang","Yellow")

# Calling Method
# c1.show_Details()
# c2.show_Details()


# Flow -> Defining a  Class -> Object Creation from the class -> calls __init__() -> self.arg1 and self.arg2 fills -> calls the method show details
# Define class → Create object → __init__ runs → Object stores data → You call a method → Method uses object’s data → Outputs result
# every Class which is created , has its own own object and self points to that particular object(Sometimes to fill that empty object ..)