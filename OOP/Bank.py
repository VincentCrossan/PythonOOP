class BankAccount():
    def __init__(self, name, accnum, balance, typeacc):
        self.name = name
        self.accnum = accnum
        self.balance = balance
        self.typeacc = typeacc

    def addfunds(self, lodgement):
        self.balance = float(self.balance) + float(lodgement)
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Invalid funds")
        else:
            self.balance = float(self.balance) - float(amount)
            print(self.balance)

    def checkbal(self):
        print(self.balance)

bankacc1 = BankAccount ("Vincent", 9556313, 500, "Student")
print(bankacc1.name)
print(bankacc1.accnum)
print(bankacc1.balance)
print(bankacc1.typeacc)
bankacc1.addfunds(250)
bankacc1.withdraw(700)
bankacc1.checkbal()



