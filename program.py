
users = {}

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Try a different one.")
        return
    password = input("Enter a new password: ")  
    users[username] = {'password': password, 'balance': 0}
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")  
    if username in users and users[username]['password'] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None

def deposit(username):
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        users[username]['balance'] += amount
        print(f"Deposit successful! New balance: {users[username]['balance']}")
    else:
        print("Invalid amount.")

def withdraw(username):
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= users[username]['balance']:
        users[username]['balance'] -= amount
        print(f"Withdrawal successful! New balance: {users[username]['balance']}")
    else:
        print("Invalid amount or insufficient balance.")

def check_balance(username):
    print(f"Your balance is: {users[username]['balance']}")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Logout")
                    option = input("Choose an option: ")
                    if option == '1':
                        deposit(user)
                    elif option == '2':
                        withdraw(user)
                    elif option == '3':
                        check_balance(user)
                    elif option == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
