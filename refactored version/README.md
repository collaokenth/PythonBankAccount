# this is the refactored version of python bank system 
# type of Implementation used was:
# Input validation and sanitization
# Error handling and exception management
# Assertions and invariants

# the list below was a before and after refactoring the python bank system and the changes of each Implementation
# starting with input validation, assertion and lastly error handling.


# 1. Input Validation

# PIN Validation
# Before:

pin = int(input(f"Please enter your 4-digit pin to get started (Numbers of attempts left: {tries}): "))

# After:

try:
    pin_input = input(f"Please enter your 4-digit pin to get started (Attempts left: {tries}): ")
    if not pin_input.isdigit() or len(pin_input) != 4:
        raise ValueError("PIN must be a 4-digit number.")
    pin = int(pin_input)
except ValueError as e:
    print(f"Error: {e}")
    
    
# Option Selection Validation

# Before:

option = int(input("Please select an option: "))

# After:

option_input = input("Please select an option: ")
if not option_input.isdigit():
    raise ValueError("Option must be a number between 1 and 4.")
option = int(option_input)


# Withdrawal Amount Validation
# Before:
logged_account.withdrawal()

# After:


try:
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit() or int(amount) <= 0:
        raise ValueError("Amount must be a positive number.")
    logged_account.withdrawal(int(amount))
except Exception as e:
    print(f"Error during withdrawal: {e}")
    
# Deposit Amount Validation

# Before:

logged_account.deposit()

# After:
try:
    amount = input("Enter amount to deposit: ")
    if not amount.isdigit() or int(amount) <= 0:
        raise ValueError("Amount must be a positive number.")
    logged_account.deposit(int(amount))
except Exception as e:
    print(f"Error during deposit: {e}")
    
# Continuation Prompt Validation
# Before:


continue_option = str(input("Would you like to continue [y/n]? "))
# After:


continue_option = input("Would you like to continue [y/n]? ").strip().lower()
if continue_option not in ["y", "n"]:
    print("Invalid input. Please choose 'y' or 'n'.")
    
# =============================================================================
# 2. Assertion

# Account Validation After Login
# Before:
    
# the revious code have no assertion present.

# After:


assert logged_account is not None, "Logged account should be set at this point."


# ===============================================================================
# 3. Error Handling

# PIN Input Error Handling
# Before:


# the previous code have no error handling present.

# After:
try:
    pin_input = input(f"Please enter your 4-digit pin to get started (Attempts left: {tries}): ")
    if not pin_input.isdigit() or len(pin_input) != 4:
        raise ValueError("PIN must be a 4-digit number.")
    pin = int(pin_input)
except ValueError as e:
    print(f"Error: {e}")
    
# Withdrawal Error Handling
# Before:

logged_account.withdrawal()
# After:


try:
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit() or int(amount) <= 0:
        raise ValueError("Amount must be a positive number.")
    logged_account.withdrawal(int(amount))
except Exception as e:
    print(f"Error during withdrawal: {e}")
    
# Deposit Error Handling
# Before:

logged_account.deposit()
# After:


try:
    amount = input("Enter amount to deposit: ")
    if not amount.isdigit() or int(amount) <= 0:
        raise ValueError("Amount must be a positive number.")
    logged_account.deposit(int(amount))
except Exception as e:
    print(f"Error during deposit: {e}")
    
# Option Selection Error Handling
# Before:


option = int(input("Please select an option: "))

# After:

try:
    option_input = input("Please select an option: ")
    if not option_input.isdigit():
        raise ValueError("Option must be a number between 1 and 4.")
    option = int(option_input)
except ValueError as e:
    print(f"Error: {e}")