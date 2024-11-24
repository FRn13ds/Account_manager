from colorama import Fore , Back , Style , init
import json
import getpass
import time 
import os

init()

header = "Tool Created By : 4nnonymous "
row1 = "Contact  : alexandre.privatechat@gmail.com "
row2 = "About Tool  : Save All of Your Accounts "

print(Fore.RED +"|"," "*45,"|")
print("|",header," "*18,"|")
print(" ","-"*45)
print("|"," "*40,"|")
print("|",row1," "*1,"|")
print(" ","-"*45)
print("|"," "*45,"|")
print("|",row2," "*4,"|")
print(" ","-"*45)

# ملف تخزين المستخدمين
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
    username = input(Style.RESET_ALL +"Enter Username: ")
    if username in users:
        print(Fore.RED +"This username is used !")
        return
    password = getpass.getpass("Enter Password: ")
    users[username] = {'password': password, 'accounts': []}
    save_users(users)
    print(Fore.GREEN +"Sgined Up with succsess !")

def login_user():
    username = input(Style.RESET_ALL +"Enter Username: ")
    password = getpass.getpass("Enter Password: ")
    if username in users and users[username]['password'] == password:
        print(Fore.GREEN +"Login With Succsess !")
        return username
    else:
        print(Fore.RED +"invaild password or username !")
        return None

def add_account(username):
    account_name = input(Fore.WHITE +"Enter the account Name (Facebook \ Instagram \ Google) ")
    account_password = getpass.getpass(Fore.WHITE +"Enter the account Password: ")
    users[username]['accounts'].append({'account_name': account_name, 'password': account_password})
    save_users(users)
    print(Fore.GREEN +"Added with succsess !")

def show_accounts(username):
    if users[username]['accounts']:
        print(Back.YELLOW +"Account linked with tool account ",Style.RESET_ALL)
        print(Fore.RED +"Seachring...")
        time.sleep(2)
        for account in users[username]['accounts']:
            print(Back.YELLOW +f"Account Name: {account['account_name']}, Password: {account['password']}",Style.RESET_ALL)
    else:
        print(Fore.RED +"No Account Linked With this User account !")

# الوظيفة الرئيسية
users = load_users()

def main():
    print(Fore.WHITE +"    Welcome to account manager !")
    print("           Please Wait...")
    time.sleep(1)
    os.system('cls')
    time.sleep(2)
    print(Fore.RED +"|"," "*45,"|")
    print("|",header," "*18,"|")
    print(" ","-"*45)
    print("|"," "*45,"|")
    print("|",row1," "*15,"|")
    print(" ","-"*45)
    print("|"," "*45,"|")
    print("|",row2," "*4,"|")
    print(" ","-"*45)
    print(Fore.BLUE +"  _    _                 _                 _            ")
    print(Fore.YELLOW +" | |  | |               | |               | |           ")
    print(Fore.RED +" | |__| | ___  _ __ ___ | |__   __ _ _ __ | |_ ___ _ __ ")
    print(Fore.BLUE +" |  __  |/ _ \| '_ ` _ \| '_ \ / _` | '_ \| __/ _ \ '__|")
    print(Fore.YELLOW +" | |  | | (_) | | | | | | | | | (_| | | | | ||  __/ |   ")
    print(Fore.RED +" |_|  |_|\___/|_| |_| |_|_| |_|\__,_|_| |_|\__\___|_|   ")	

   
    while True:
         action = input(Fore.BLUE +"choose an action : [1] Sgin Up [2] Login  [3] Add Account  [4] Show Accounts  [5] Exit  :")
         if action == '1':
            register_user()
         elif action == '2':
            username = login_user()
         elif action == '3':
            if username:
                add_account(username)
            else:
                print(Fore.RED +"Please Sgin Up First !")
         elif action == '4':
            if username:
                show_accounts(username)
            else:
                print(Fore.RED +"You must be logged in !")
         elif action == '5':
            print(Fore.RED+"   / \   __ _  __ _ _ __ | |__   __ _ _ __ | |_ ___ _ __")
            print(Fore.BLUE +"  / _ \ / _` |/ _` | '_ \| '_ \ / _` | '_ \| __/ _ \ '__|")
            print(Fore.YELLOW +"/ ___ \ (_| | (_| | | | | | | | (_| | | | | ||  __/ |  ")
            print(Fore.RED +"/_/   \_\__,_|\__,_|_| |_|_| |_|\__,_|_| |_|\__\___|_")

            print(Fore.GREEN +"Thanks for using our tool !")
            break
         else:
            print(Fore.RED +"Try again ! ")

if __name__ == "__main__":
    main()
