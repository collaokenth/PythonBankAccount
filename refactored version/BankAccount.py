class BankAccount:
    def __init__(self, pin, account_holder, balance):
        self.pin = pin
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"{self.account_holder}, your current balance is {self.balance:.2f}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal cannot be processed.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Your new balance is {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful! Your new balance is {self.balance:.2f}")
