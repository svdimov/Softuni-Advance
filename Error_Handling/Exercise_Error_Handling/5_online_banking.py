class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


user_data = input().split(', ')
pin = user_data[0]
balance = int(user_data[1])
age = int(user_data[2])
LEGAL_AGE = 18

while True:
    user_data = input().split("#")
    cmd = user_data[0]
    if cmd == "End":
        break
    if cmd == "Send Money":
        amount = int(user_data[1])
        current_pin = user_data[2]

        if balance < amount:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin != current_pin:
            raise PINCodeError("Invalid PIN code")
        if age < LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        balance -= amount
        print(f"Successfully sent {amount:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    if cmd == "Receive Money":
        amount = int(user_data[1])/2
        if amount < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        balance+= amount/2
        print(f"{amount:.2f} money went straight into the bank account")
