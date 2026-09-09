class bank:
    def __init__(self, balance):

        self.__balance__ = "2000"

    def deposit (self, balance):
        print(f"depositing {balance} to account")


    def show_balance(self):
        print("balance:", self.__balance__)

    def addmoney(self, balance):
        self.__balance__ = balance

bankaccount = bank("2000")
bankaccount.show_balance()
bankaccount.deposit(500)
bankaccount.addmoney(2500)
bankaccount.show_balance()

