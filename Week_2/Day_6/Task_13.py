class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    def set_owner(self, owner):
        if owner.strip():
            self.__owner = owner
        else:
            print("Owner's name cannot be empty.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")


if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount("123456789", 1000, "John Doe")

    # Displaying initial account information
    print("Initial Account Information:")
    print("Account Number:", account.get_account_number())
    print("Owner:", account.get_owner())
    print("Balance:", account.get_balance())

    # Depositing funds
    account.deposit(500)
    print("\nAfter Deposit:")
    print("Balance:", account.get_balance())

    # Withdrawing funds
    account.withdraw(200)
    print("\nAfter Withdrawal:")
    print("Balance:", account.get_balance())

    # Attempting to set negative balance
    account.set_balance(-500)

    # Attempting to set empty owner name
    account.set_owner("")

    # Displaying final account information
    print("\nFinal Account Information:")
    print("Account Number:", account.get_account_number())
    print("Owner:", account.get_owner())
    print("Balance:", account.get_balance())
