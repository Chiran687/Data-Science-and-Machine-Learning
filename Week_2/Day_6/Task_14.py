class BankAccount:
    def __init__(self, account_number, balance, owner):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner = owner

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        try:
            if balance >= 0:
                self.__balance += balance
            elif balance < 0:
                print("Balance must be positive number.")
        except Exception as e:
            print(e)

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        if owner != None:
            self.__owner = owner.strip()
        else:
            print("Owner name is Empty.")

    def withdrawl(self, withdraw_balance):
        if withdraw_balance > self.__balance:
            print("Insufficient Balance.")
        else:
            self.remaining_balance = self.__balance - withdraw_balance
            print(
                f"Transaction doone of {withdraw_balance}, remaining balance is {self.remaining_balance}."
            )
            print(self.remaining_balance)
            return self.remaining_balance


if __name__ == "__main__":
    bankaccount = BankAccount(123456, 0, "Jalak")

    print("Initial Startup of Banking.")
    print(f"The account number is {bankaccount.get_account_number()}.")
    print(
        f"The owner of account is {bankaccount.get_owner()} with balance {bankaccount.get_balance()}."
    )

    bankaccount.set_balance(5000)
    print(f"Balance after deposit is {bankaccount.get_balance()}")

    while True:
        try:
            withdraw = int(input("Give the balance to withdraw: "))
            if withdraw > 0:
                bankaccount.withdrawl(withdraw)
                bankaccount.set_balance(-withdraw)
                break
            else:
                ("Please double check balance.")
        except Exception as e:
            print(e)

    print("\nFinal Account Information:")
    print("Account Number:", bankaccount.get_account_number())
    print(
        f"Owner: {bankaccount.get_owner()} with remaining balance {bankaccount.withdrawl(withdraw)}"
    )
