class Account:
    account_number_generator = []
    account_number_identification = 1

    # ATTRIBUTES
    def __init__(self, account_number, account_balance, account_holder):
        self.account_balance = 0
        self.account_holder = account_holder

        if account_number is None:
            self.account_number = len(Account.account_number_generator) + 1
            Account.account_number_generator.append(self.account_number)
            Account.account_number_identification += 1
            print("Your new account number is", self.account_number)
        else:
            self.account_number = Account.account_number_identification

    # METHODS
    def deposit(self, amount):
        self.account_balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("You do not have enough cash for this withdrawal")

    def check_balance(self):
        return self.account_balance

# Create instances of the Account class
Maryam_account = Account(None, 0, 'Maryam')
Adeola_account = Account(None, 0, 'Adeola')

# Perform deposit and withdraw operations
Maryam_account.deposit(30000)
print("Current balance:", Maryam_account.check_balance())

Adeola_account.check_balance()
print("Current balance:", Adeola_account.check_balance())

Adeola_account.deposit(30000)
print("Current balance:", Adeola_account.check_balance())

Adeola_account.withdraw(540000)
print("Current balance:", Maryam_account.check_balance())

print("Adeola_account number:", Adeola_account.account_number)