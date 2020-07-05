# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?
class Account(object):
    def __init__(self,name,account_number,initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def data_print(self):
        s = '%s, %s, balane :: %s' %(self.name, self.no, self.balance)
        print(s)

a1 = Account('Keshab Saud','5143558474275487',20000)
a1.deposit(10000)
a1.withdraw(4000)
a1.withdraw(9000)
a1.data_print()
