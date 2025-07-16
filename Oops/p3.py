'''
Encapsulation ::
-> Wrapping up data and methods into one single unit class and controlling the access to the data
-> Think of putting secret passwords into a locker :
  -> You lock it (Make it Private)
  -> You access it with a key (Getter,setter)
'''
'''
# Wihout getter and setter
class Bank:
    def __init__(self):
        self.__balance = 1000

b = Bank()

# print(b.__balance) # raises an error as we are trying to access the private variable

# using name mangling trick (objectName._classNameprivate)
print("Bank_Balance : ",b._Bank__balance)
'''
# With getter and setter
class Account:
    def __init__(self, acc_holder, acc_balance):
        self.__acc_holder = acc_holder      # private
        self.__acc_balance = acc_balance    # private

    # Method to check if account is valid
    def valid_acc(self, min_bal):
        if self.__acc_balance >= min_bal:
            print("✅ Valid Account!")
        else:
            print("❌ Not a Valid Account!")

    # Setter for balance
    def set_balance(self, bal):
        if bal > 0:
            self.__acc_balance = bal
        else:
            print("❌ Invalid Amount! Please enter positive balance.")

    # Getter for info
    def get_Info(self):
        print(f"Account Holder: {self.__acc_holder}")
        print(f"Account Balance: ₹{self.__acc_balance}")


acc1 = Account("Mike Jorsey",42010)
acc2 = Account("Dextrr",32800)

acc1.get_Info()
acc2.get_Info()

#setting the balance
acc1.set_balance(37600)
acc1.get_Info()

# Check wheather account is valid now or not
acc1.valid_acc(40000)
acc2.valid_acc(20000)