import os
import time


USERS = {
    "ahmed": ("1234", 1500.00),
    "mona":  ("abcd", 2500.50),
}

MAX_LOGIN_ATTEMPTS = 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_float(value):
    """Check if a value is a number (float) without try/except."""
    if value.replace(".", "", 1).isdigit():
        return True
    return False

def add_user():
    """Add a new user to the ATM system."""
    print("=== Add New User ===")
    new_username = input("Enter new username: ").strip()
    if new_username in USERS:
        print("Username already exists.\n")
        time.sleep(2)
        clear_screen()
        return
    
    new_password = input("Enter password: ").strip()
    initial_balance_str = input("Enter initial balance: ").strip()
    
    if not is_float(initial_balance_str):
        print("Invalid balance amount.\n")
        time.sleep(2)
        clear_screen()
        return
    
    initial_balance = float(initial_balance_str)
    USERS[new_username] = (new_password, initial_balance)
    print(f"User '{new_username}' added successfully with balance {initial_balance:.2f} EGP.\n")
    time.sleep(2)
    clear_screen()

def login():
    """User login function."""
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        user = USERS.get(username)
        if user and user[0] == password:
            print(f"Login successful. Welcome {username}!\n")
            time.sleep(1)
            clear_screen()
            return username
        else:
            attempts += 1
            print(f"Invalid credentials. Attempt {attempts}/{MAX_LOGIN_ATTEMPTS}\n")
            time.sleep(1)
            clear_screen()
    print("Maximum login attempts reached. Please try again later.")
    return None

def show_menu():
    print("Choose an operation:")
    print("1 - Check Balance")
    print("2 - Withdraw")
    print("3 - Deposit")
    print("4 - Add New User")
    print("5 - Exit")

def format_balance(b):
    return f"{b:.2f} EGP"

def atm_session(username):
    """Main ATM session after login."""
    balance = USERS[username][1]
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Current balance:", format_balance(balance), "\n")
            time.sleep(2)
            clear_screen()

        elif choice == "2":
            amt_str = input("Enter withdrawal amount: ").strip()
            if not is_float(amt_str):
                print("Please enter a valid number.\n")
                time.sleep(1)
                clear_screen()
                continue
            amt = float(amt_str)
            if amt <= 0:
                print("Enter an amount greater than zero.\n")
            elif amt > balance:
                print("Insufficient balance.\n")
            else:
                balance -= amt
                print(f"Withdrawal successful. New balance: {format_balance(balance)}\n")
            time.sleep(2)
            clear_screen()

        elif choice == "3":
            amt_str = input("Enter deposit amount: ").strip()
            if not is_float(amt_str):
                print("Please enter a valid number.\n")
                time.sleep(1)
                clear_screen()
                continue
            amt = float(amt_str)
            if amt <= 0:
                print("Enter an amount greater than zero.\n")
            else:
                balance += amt
                print(f"Deposit successful. New balance: {format_balance(balance)}\n")
            time.sleep(2)
            clear_screen()

        elif choice == "4":
            add_user()

        elif choice == "5":
            print("Exiting. Goodbye!")
            USERS[username] = (USERS[username][0], balance)
            time.sleep(1)
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.\n")
            time.sleep(1)
            clear_screen()

def main():
    clear_screen()
    print("=== Simple ATM Simulator ===")
    user = login()
    if user:
        atm_session(user)

if __name__ == "__main__":
    main()
