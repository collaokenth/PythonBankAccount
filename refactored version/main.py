from BankAccount import BankAccount

# Sample bank accounts
bank_accounts = [
    BankAccount(1234, "Josh Martinez", 10000),
    BankAccount(4567, "Emma Watson", 30000),
    BankAccount(6789, "John Warne", 5000)
]

logged_account = None
tries = 3

print("Hello! Welcome to Humber Bank Terminal!")

# Log in user
while True:
    try:
        pin_input = input(f"Please enter your 4-digit pin to get started (Attempts left: {tries}): ")
        if not pin_input.isdigit() or len(pin_input) != 4:
            raise ValueError("PIN must be a 4-digit number.")

        pin = int(pin_input)
        
        # Validate pin against accounts
        logged_account = next((account for account in bank_accounts if account.pin == pin), None)

        if logged_account:
            break
        else:
            print("Invalid PIN. Please try again.")

    except ValueError as e:
        print(f"Error: {e}")

    tries -= 1
    if tries == 0:
        print("Limit of attempts exceeded. Access Denied.")
        exit()

assert logged_account is not None, "Logged account should be set at this point."

# Main menu
while True:
    try:
        print(f"\nWelcome back, {logged_account.account_holder}. How may we help you today?")
        print("[1] Display Balance\n[2] Withdrawal\n[3] Make a Deposit\n[4] Exit")

        option_input = input("Please select an option: ")
        if not option_input.isdigit():
            raise ValueError("Option must be a number between 1 and 4.")

        option = int(option_input)

        match option:
            case 1:
                logged_account.display_balance()

            case 2:
                try:
                    amount = input("Enter amount to withdraw: ")
                    if not amount.isdigit() or int(amount) <= 0:
                        raise ValueError("Amount must be a positive number.")
                    logged_account.withdrawal(int(amount))
                except Exception as e:
                    print(f"Error during withdrawal: {e}")

            case 3:
                try:
                    amount = input("Enter amount to deposit: ")
                    if not amount.isdigit() or int(amount) <= 0:
                        raise ValueError("Amount must be a positive number.")
                    logged_account.deposit(int(amount))
                except Exception as e:
                    print(f"Error during deposit: {e}")

            case 4:
                print("Thank you for using our program!")
                exit()

            case _:
                print("Invalid option. Please select a valid option.")
                continue

        # Prompt for continuation
        while True:
            continue_option = input("Would you like to continue [y/n]? ").strip().lower()
            if continue_option == "n":
                print("Thank you for using our program!")
                exit()
            elif continue_option == "y":
                break
            else:
                print("Invalid input. Please choose 'y' or 'n'.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
