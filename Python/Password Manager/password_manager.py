from cryptography.fernet import Fernet  # type: ignore

# This function is used to create encryption key in key.key file 
# Function to create encryption key 
'''
def create_key(): 
    key = Fernet.generate_key()
    with open('Projects\\Password Manager\\key.key', 'wb') as key_file:
        key_file.write(key)

create_key()
'''

# Load key 
def load_key():
    file = open("Projects\\Password Manager\\key.key", 'rb')
    key = file.read()
    file.close()
    return key 

# Load key
key = load_key() 
# Create fernet key 
fer = Fernet(key)


# Function to view password
def view_password():
    with open('Projects\\Password Manager\\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            account_name, password = data.split("|")
            print(f"Username: {account_name}\nPassword: {fer.decrypt(password.encode()).decode()}\n----------")


# Function to add new password
def add_password():
    # Add password to the password file and if that doesn't exist create it. 
    # Get the name of the password i.e which website / app it's for 
    name = input("Account Name: ").rstrip()
    # Get the content of the password
    password = input("Password: ").rstrip()
    with open('Projects\\Password Manager\\passwords.txt', 'a') as f: 
        f.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")

# Ask user for which mode they want to be in
while True:
    mode = input("Exit (e)\nView password (view) / Add password (add): ").lower()
    if mode == "e": 
        break
    elif mode == "view":
        view_password()
    elif mode == "add":
        add_password()
    else:
        print("Enter a valid mode.")
        continue