class Account:
    def __init__(self,balance,acc_number):
        self.balance = balance
        self.accountNumber = acc_number

    def debit(self,balance):
        self.balance -= balance
        print("Rs.", balance, "was debited")

    def credit(self, balance):
        self.balance += balance
        print("Rs.", balance, "was credited")

    def rem_balance(self):
        print("Your remaining balance is:" + str(self.balance))


a1 = Account(10000,123)
a1.debit(5000)
a1.credit(2000)
a1.rem_balance()
