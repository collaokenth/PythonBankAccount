class BankAccount:

    def __init__(self, pin, account_holder, balance=0):
        self.balance = balance
        self.pin = pin
        self.account_holder = account_holder

    def display_balance(self):
        print(f"{self.account_holder}, your current balance is {self.balance:.2f}")

    def deposit(self):

        try:
            amount = float(input("Enter amount to deposit: "))
        except(ValueError):
            print("Invalid input. Please type a number.")
            return
        
        self.balance += amount
        print(f"Deposit completed. Your current balance is {self.balance:.2f}")
    
    def withdrawal(self):

        try:
            option = int(input("Enter the amount you want to withdraw:\n[1]20\n[2]40\n[3]60\n[4]80\n[5]100\n[6]Custom(Enter amount)\n"))
        except(ValueError):
            print("Invalid input. Please type a valid option")
            return
        
        amount = 0

        match option:
            case 1:
                amount = 20
            case 2:
                amount = 40
            case 3:
                amount = 60
            case 4:
                amount = 80
            case 5:
                amount = 100
            case _:
                amount = option

        if amount > self.balance:
            print("You don't have enough funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal completed. Your current balance is {self.balance:.2f}")
