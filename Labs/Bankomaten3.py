import random

class Account:
    #Skapa ett konto object
    def __init__(self, id, balance = 0, ränta = 3.4):
        self.id = id
        self.balance = balance
        self.ränta = ränta
    
    def getId(self):
        return self.id
    
    def getBalance(self):
        return self.balance
    
    def getRänta(self):
        return self.ränta
    
    def getMånadsRänta(self):
        return self.ränta / 12
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
    
    def getMånadsRänta(self):
        return self.balance * self.getMånadsRänta()

def main():
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(accounts)

    while True:
        id = int(input("Skriv in ditt valda kontonummer"))

        while id < 1000 or id > 9999:
            id = int(input("ERROR: Ej valbart kontonummer.. Testa igen: "))
            
