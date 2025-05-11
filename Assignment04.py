# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"

    def __init__(self , account_holder):
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {self.bank_name}")


acc1 = Bank("Aiza")
acc2 = Bank("Amna")

Bank.change_bank_name("National Bank of Pakistan")

acc1.display()
acc2.display()
