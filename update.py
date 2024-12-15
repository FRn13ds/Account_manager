from colorama import Fore, Back, Style, init
import json
import getpass
import time
import os

init()

header = "Tool Created By: 4nnonymous"
row1 = "Contact: alexandre.privatechat@gmail.com"
row2 = "About Tool: Save All of Your Accounts"
row3 = "            Version: 0.2             "

print(Fore.RED + "|", " " * 43, "|")
print("|", header, " " * 15, "|")
print(" ", "-" * 45)
print("|", " " * 43, "|")
print("|", row1, " " * 2, "|")
print(" ", "-" * 45)
print("|", " " * 43, "|")
print("|", row2, " " * 5, "|")
print(" ", "-" * 45)
print(Fore.GREEN + "|", row3, " " * 5, "|")
print(" ", "-" * 45)

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

def register_user():
    username = input(Style.RESET_ALL + "Enter Username: ")
    if username in users:
        print(Fore.RED + "This username already in use !")
        return
    password = getpass.getpass("Enter Password: ")
    users[username] = {'password': password, 'accounts': []}
    save_users(users)
    print(Fore.GREEN + "Signed Up with success!")

def login_user():
    username = input(Style.RESET_ALL + "Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    if username in users and users[username]['password'] == password:
        print(Fore.GREEN + "Login With Success!")
        return username
    else:
        print(Fore.RED + "Invalid password or username!")
        return None

def add_account(username):
    if username not in users:
        print(Fore.RED + "User does not exist!")
        return
    account_type = input("Account Type [1] Facebook [2] Instagram [3] Google [4] Steam [5] Epic Games [6] Telegram [7] WhatsApp ")
    account_name = input(Fore.WHITE + "Enter the account Name: ")
    account_password = getpass.getpass(Fore.WHITE + "Enter the account Password: ")
    users[username]['accounts'].append({'account_name': account_name, 'account_type': account_type, 'password': account_password})
    save_users(users)
    print(Fore.GREEN + "Added with success!")


def show_accounts(username):
    if username not in users:
        print(Fore.RED + "User does not exist!")
        return
    if 'accounts' not in users[username] or not users[username]['accounts']:
        print(Fore.RED + "No Account Linked With this User account!")
        return
    print(Back.YELLOW + "Account linked with tool account ", Style.RESET_ALL)
    print(Fore.RED + "Searching...")
    time.sleep(2)
    for account in users[username]['accounts']:
        account_type = account.get('account_type', 'Unknown')
        account_name = account.get('account_name', 'Unknown')
        account_password = account.get('password', 'Unknown')
        print(Back.YELLOW + f"Account Type: {account_type}, Account Name: {account_name}, Password: {account_password}", Style.RESET_ALL)

users = load_users()

def main():
    username = None
    print(Fore.WHITE + "             Welcome to account manager!")
    print("                                Please Wait...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print(Fore.RED + "|", " " * 43, "|")
    print("|", header, " " * 15, "|")
    print(" ", "-" * 45)
    print("|", " " * 43, "|")
    print("|", row1, " " * 2, "|")
    print(" ", "-" * 45)
    print("|", " " * 43, "|")
    print("|", row2, " " * 5, "|")
    print(" ", "-" * 45)
    print(Fore.GREEN + "|", row3, " " * 5, "|")
    print(" ", "-" * 45)
    print(Fore.RED + " █████╗  ███████║██║██║     ██║     ███████║██║     ██║  ███╗")
    print(Fore.GREEN + "██╔══██╗ ██╔════╝██║██║     ██║     ██╔════╝██║     ██║ ██╔██╗")
    print(Fore.WHITE + "███████║ █████╗  ██║██║     ██║     █████╗  ██║     █████╔╝██║")
    print(Fore.YELLOW + "██╔══██║ ██╔══╝  ██║██║     ██║     ██╔══╝  ██║     ██╔═██╗██║")
    print(Fore.BLUE + "██║  ██║ ██║     ██║███████╗███████╗██║     ███████╗██║  ██╗██║")
    print(Fore.RED + "╚═╝  ╚═╝ ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝")

    while True:
        action = input(Fore.BLUE + "Choose an action: [1] Sign Up [2] Login  [3] Add Account  [4] Show Accounts  [5] Exit: ")
        if action == '1':
            register_user()
        elif action == '2':
            username = login_user()
        elif action == '3':
            if username:
                add_account(username)
            else:
                print(Fore.RED + "Please Sign Up or Log In First!")
        elif action == '4':
            if username:
                show_accounts(username)
            else:
                print(Fore.RED + "You must be logged in!")
        elif action == '5':
            print("        .--.")
            print("       |o_o |")
            print("       |:_/ |")
            print("      //   \ \\")
            print("     (|     | )")
            print("    /'\\_   _/`\\")
            print("    \\___)=(___/")
            print(Fore.GREEN + "Thanks for using our tool!")
            break
        else:
            print(Fore.RED + "Try again!")

if __name__ == "__main__":
    main()