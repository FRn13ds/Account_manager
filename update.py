import bcrypt
import json
import getpass
import time
import os
from colorama import Fore, Back, Style, init

init()

header = "Tool Created By: FRn13ds"
row1 = "Contact: med.yassine.salmi110@gmail.com"
row2 = "About Tool: Save All of Your Accounts"
row3 = "            Version: 0.3             "

logo = '''
 █████╗ ███████╗ █████╗ ██╗███████╗██╗  ██╗██╗   ██╗
██╔══██╗██╔════╝██╔══██╗██║╚════██║██║  ██║██║   ██║
███████║███████╗███████║██║    ██╔╝███████║██║   ██║
██╔══██║╚════██║██╔══██║██║   ██╔╝ ██╔══██║██║   ██║
██║  ██║███████║██║  ██║██║   ██║  ██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝  ╚═╝  ╚═╝ ╚═════╝
'''

store_file = 'users.json'

def load_users():
    try:
        with open(store_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(store_file, 'w') as file:
        json.dump(users, file, indent=4)

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(stored_password, entered_password):
    try:
        return bcrypt.checkpw(entered_password.encode(), stored_password.encode())
    except ValueError:
        print(Fore.RED + "Stored password is invalid. Please reset your data.")
        return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    clear_screen()
    print(Fore.GREEN + logo)
    print(Fore.RED + "|", " " * 43, "|")
    print("|", header, " " * 18, "|")
    print(" ", "-" * 45)
    print("|", " " * 43, "|")
    print("|", row1, " " * 3, "|")
    print(" ", "-" * 45)
    print("|", " " * 43, "|")
    print("|", row2, " " * 5, "|")
    print(" ", "-" * 45)
    print(Fore.GREEN + "|", row3, " " * 5, "|")
    print(" ", "-" * 45)

def display_registration_interface():
    display_header()
    print(Fore.GREEN + "\n=== User Registration ===\n")
    username = input(Fore.WHITE + "Enter Username: ")
    password = getpass.getpass(Fore.WHITE + "Enter Password: ")
    return username, password

def display_login_interface():
    display_header()
    print(Fore.BLUE + "\n=== User Login ===\n")
    username = input(Fore.WHITE + "Enter Username: ")
    password = getpass.getpass(Fore.WHITE + "Enter Password: ")
    return username, password

def register_user(users):
    username, password = display_registration_interface()
    if username in users:
        print(Fore.RED + "This username is already in use!")
        return
    hashed_password = hash_password(password).decode()
    users[username] = {'password': hashed_password, 'accounts': []}
    save_users(users)
    print(Fore.GREEN + "Signed up successfully!")

def login_user(users):
    username, password = display_login_interface()
    if username in users and verify_password(users[username]['password'], password):
        print(Fore.GREEN + "Logged in successfully!")
        return username
    else:
        print(Fore.RED + "Invalid password or username!")
        return None

def add_account(users, username):
    if username not in users:
        print(Fore.RED + "User does not exist!")
        return
    account_type = input("Account Type [Facebook, Instagram, Google, Steam, Epic Games, Telegram, WhatsApp]: ")
    account_name = input(Fore.WHITE + "Enter the account name: ")
    account_password = getpass.getpass(Fore.WHITE + "Enter the account password: ")
    users[username]['accounts'].append({'account_name': account_name, 'account_type': account_type, 'password': account_password})
    save_users(users)
    print(Fore.GREEN + "Account added successfully!")

def show_accounts(users, username):
    if username not in users:
        print(Fore.RED + "User does not exist!")
        return
    if not users[username]['accounts']:
        print(Fore.RED + "No accounts linked with this user account!")
        return
    print(Back.YELLOW + "Accounts linked with your tool account:", Style.RESET_ALL)
    print(Fore.RED + "Fetching... Please wait.")
    time.sleep(2)
    for account in users[username]['accounts']:
        account_type = account.get('account_type', 'Unknown')
        account_name = account.get('account_name', 'Unknown')
        account_password = account.get('password', 'Unknown')
        print(Back.YELLOW + f"Account Type: {account_type}, Account Name: {account_name}, Password: {account_password}", Style.RESET_ALL)

def reset_data_confirmation():
    print(Fore.RED + "\n=== Reset Data ===\n")
    confirm = input("Are you sure you want to reset all user data? Type 'yes' to confirm: ")
    if confirm.lower() == 'yes':
        save_users({})
        print(Fore.GREEN + "All data has been reset.")
    else:
        print(Fore.YELLOW + "Data reset canceled.")

def main():
    users = load_users()
    username = None
    while True:
        action = input(Fore.BLUE + "\nChoose an action: \n[1] Sign Up \n[2] Login \n[3] Add Account \n[4] Show Accounts \n[5] Reset Data \n[6] Exit\nEnter your choice: ")
        if action == '1':
            register_user(users)
        elif action == '2':
            username = login_user(users)
        elif action == '3':
            if username:
                add_account(users, username)
            else:
                print(Fore.RED + "Please sign up or log in first!")
        elif action == '4':
            if username:
                show_accounts(users, username)
            else:
                print(Fore.RED + "You must be logged in!")
        elif action == '5':
            reset_data_confirmation()
        elif action == '6':
            display_header()  # Display the header/logo before exiting
            print(Fore.GREEN + "   Thank you for using our tool! Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option! Try again.")

if __name__ == "__main__":
    main()

