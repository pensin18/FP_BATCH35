class Bank:
    bank_name = 'Global Bank'

    def __init__(self,name,accountno,balance):
        self.name = name
        self.id = accountno
        self.balance= balance
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

a1= Bank('Alice',12345,1000)
print(a1.get_balance())  # Output: 1000

class Broker:
    broker_name = 'ibk'
    stock_prices = {'tsla':100,'amzn':500,'nifty':700,'ongc':6000}

    def __init__(self,name,no,balance):
        self.name = name
        self.id = no
        self.wallet = balance
        self.portfolio= {}
    def buy(self,name):
        found = self.stock_prices.get(name)
        if found:
            if self.wallet >= found:
