from cryptography.fernet import Fernet
import base64

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
# encode takes your string and turns it into bytes
# key = load_key() + master_pwd.encode()

key = base64.urlsafe_b64encode(key)
fer = Fernet(key)


def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            # THIS GAVE ME AN ERROR
            # user, passw = data.split("|")  # Returns in a list form.
            user = data.split("|")
            passw = data.split("|")
            print("User:", user, "Password:", fer.decrypt(passw.encode()))


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # with automatically closes the file after opening.
    # modes: w - write - overrides /
    #       'r' read-only /
    #       'a' append - add soemthing to the end of the existing file. if non exist, creates a new one.
    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones? (view,add, q to quit) ")

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
    else:
        print("Invalid mode.")
        continue
