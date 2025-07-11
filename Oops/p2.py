'''
    Class Variable :
    -> defined out of the method and inside the class.
    -> shared by the all of the Method(Object)
    -> It has just one Copy
    -> accessed using className.variable_name
    Instance Variable :
    -> Created each time for each Object creation
    -> Accessed using self.arg
'''

class Employee:
    firm = 'Swish' # class attribute
    def __init__(self,name,salary):
        # instance attributes
        self.name = name
        self.salary = salary

    def getter(self):
        print(f"Employee: {self.name} , Salary:{self.salary} , Company: {Employee.firm}")

e1 = Employee("Zerox",98000)
e2 = Employee("Dextrr",76000)
e3 = Employee("Johnson",72300)
e4 = Employee("JackSon",89000)

e1.getter()
e2.getter()
e3.getter()
e4.getter()

