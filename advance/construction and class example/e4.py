""" Define a class BankAccount with attributes account_holder and balance. Add methods deposit() and withdraw() to update the balance.
 """
class BankAccount:
    def __init__ (self, Account_holder, Balance):
        self.account_holder = Account_holder
        self.balance = Balance
    def withdraw(self):
        a= int(input("Enter withdraw Amount: "))
        if (a>0 and a<=self.balance):
            self.balance = self.balance - a
            print("Successfully withdraw")
            print("balance remaining", self.balance)
        else:
            print("Invald balance")
    
    def deposit(self):
        a= int(input("Enter deposit Amount: "))
        if a>0:
            self.balance = self.balance + a
            print("Successfully deposited")
            print("balance remaining", self.balance)
        else:
            print("Invald deposit amount")

p1 = BankAccount("Taha", 1560)
p1.withdraw()
p1.deposit()