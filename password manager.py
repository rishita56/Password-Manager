from cryptography.fernet import Fernet #encrypts text

def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key




key = load_key()  
fer= Fernet(key)

def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data=line.strip() #rstrip is used to eliminate the \n and also strip can be used
            if "|" in data:
                user, passw = data.split("|")  # Split by pipe operator
                print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")
            else:
                print(f"Skipping line due to incorrect format: {line}")          
           
def add():
    name=input("Account Name: ")
    pwd= input("Password: ")

    with open("password.txt",'a') as f:  #a is used for appending, if file does not exists it creates and adds else adds att the end of the existing file
        #w stands for write, one more mode, r stands for read to just read file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones or quit?(add/view/q) ").lower()

    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()
