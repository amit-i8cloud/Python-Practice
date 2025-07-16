'''
Inheritance :
-> ITs when a child class inherits the properties and methods of the parent class
-> It allows us to reuse the code from another class
-> Code Reusability
-> Less Deuplication
-> A child class can inherit and access everything from the parent class except private members(__name)
-> Organized due to fact that different features have differnt classes so by searching the class name we can go the that class.
'''

# Without Inheritance
# class Parent:
#     def method1(self):
#         print("Parent Class !!")
#
# class Child:
#     def method2(self):
#         print("Child Class !!")
# :: Child class now have access to all public and protected members of the parent class .
# We will discuss them later one by one .

# obj = Child()
# obj.method2()
# obj.method1() # cant access as till now we had not inherited the parent class .

# With Inheritance
# class Parent:
#     def method1(self):
#         print("Parent Class !!")
#
# class Child(Parent):
#     def method2(self):
#         print("Child Class !!")
#
# obj = Child()
# obj.method2()
# obj.method1() # can access as now we had not inherited the parent class .

'''              Types of Inheritance        '''
'''
Single Inheritance :: 
-> One child class inherits from one parent class
'''
# class i8Cloud:
#     def employee(self):
#         print("Employee from i8Cloud !!")
#
#
# class Meta(i8Cloud):
#
#     # below is Overwriting the existing the parent child content
#     # def employee(self):
#     #     print("Employee from Facebook")
#
#     # below is the extending functionality of the Parent class
#     # def employee(self):
#     #     super().employee()
#     #     print("Its a Good Employee !!")
#
#     def employee2(self):
#        # super().employee()   # calling the function of the parent class using super
#         self.employee()  # calling the function of the parent class
#         print("Employee from Meta !!")
#
# obj = Meta()
# # print(obj.employee())
# print(obj.employee2())

'''
Multilevel Inheritance :: 
-> In Multilevel Inheritance, a class inherits from a child class, which itself inherited from another class.
'''
# class A:
#     def user1(self):
#         print("User from the Class-A")
# class B(A):
#     def user1(self):
#         super().user1()
#         print("User1 is from Brazil")
#     def user2(self):
#         print("User from the Class-B")
#
# class C(B):
#     def user1(self):
#         super().user1()
#         print("User1 is from -- South America --")
#     def user2(self):
#         self.user1()
#         super().user1()
#         print("User from the Class-C")
#
# obj = C()
# obj.user2()


'''
Hierarchical  Inheritance :: 
-> In Hierarchical Inheritance, multiple child classes inherit from the same parent class.
'''
# class A:
#     def user1(self):
#         print("This is user from class-A")
# class B(A):
#     def user2(self):
#         print("This is user from class-B")
# class C(A):
#     def user1(self):
#       #  super().user1()
#         print("This is Halloweeen !!")
#     def user3(self):
#         print("This is user from class-C")
#
# obj = C()
# obj.user1()
# # obj.user2()
# obj.user3()

'''
Multiple Inheritance :: 
-> A single child class inherits from more than one parent class.
'''
class A:
    def user1(self):
        print("This is user from class-A")
class B:
    def user2(self):
        print("This is user from class-B")
class C(A,B):
    def user1(self):
        super().user1()
        print("This is Halloweeen for user1 !!")
    def user2(self):
        super().user2()
        print("This is HAppy ThanksGiving for user2 !!")
    def user3(self):
        self.user1()
        self.user2()
        print("This is user from class-C")

obj = C()
obj.user3()

