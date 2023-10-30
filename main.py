from BankAccount import BankAccount

bank_accounts = [BankAccount(1234, "Josh Martinez", 10000), BankAccount(4567, "Emma Watson", 30000), BankAccount(6789, "John Warne", 5000)]
logged_account = None
tries = 3

print("Hello! Welcome to Humber Bank Terminal!")

#Logs in user
while True:

    try:
        pin = int(input(f"Please enter your 4-digit pin to get started (Numbers of attempts left: {tries}): "))
    except (ValueError):
        print("Please enter a 4-digit pin. Make sure to type numbers")
        continue
    tries -= 1

    for account in bank_accounts:
        if account.pin == pin:
            logged_account = account
    if logged_account != None:
        break
    if tries == 0:
        print("Limit of attempts excceded. Access Denied")
        exit()

#Main menu
while True:
    print(f"Welcome back, {logged_account.account_holder}. How may we help you today?")

    option = int(input("[1]Display Balance\n[2]Withdrawal\n[3]Make a deposit\n[4]Exit\n"))
    
    match option:
        case 1:
            logged_account.display_balance()
        case 2:
            logged_account.withdrawal()
        case 3:
            logged_account.deposit()
        case 4:
            print("Thank you for using our program!")
            exit()
        case _:
            print("Invalid option. Please try again.")
            continue
    
    while True:
        try:
            continue_option = str(input("Would you like to continue [y/n]? "))
        except(ValueError):
            print("Please choose a valid option.")
            continue
        if continue_option.lower() == "n":
            print("Thank you for using our program!")
            exit()
        elif continue_option.lower() == "y":
            break
        else:
            print("Please choose a valid option.")
            continue
