class Account:
    def __init__(self, id_: int, name: str, balance: int = 0)->None:
        self.balance = balance
        self.name = name
        self.id = id_

    def credit(self,amount)->int:
        self.balance += amount
        return self.balance
    def debit(self,amount)->int or str:

        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return f"Amount exceeded balance"

    def info(self)->str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
print('=================')
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())