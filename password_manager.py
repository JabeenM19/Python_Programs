
master_pwd = input("master password: ")

def view():
     with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line # line.rstrip() will strip of space
            # split user and password
            user, passw = data.split("|")
            print("user:",user,",","password:", passw)
def add():
    name= input("Account Name: ")
    pwd = input("Password: ")
    #file = open('passwords.txt', 'a') # to get the file in our code. youcan also use with keyword also because benefit is  python automatically closes the file after we are done or else we have to manually close the file if we use just open()
    #file.close()
    ##(filename , mode to open file(there are many modes but main are a,r,w))
    with open('passwords.txt', 'a') as f:
        f.write(name +"|" + " " + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing one (view, add)?  press q to quit ")
    if mode =="view":
        view()
    elif mode =="add":
        add()
    elif mode == "q":
        quit()
    else:
        print("Invalid mode.")
        continue

#Password encryption:




