while True:
    print ("Welcome to the Random Memory Receiver also known as RMR")
    input("Please register. Press enter to continue")
    while True:
        forename = input ("what is your forename: ")
        surname = input ("what is your surname: ")
        register_username = input ("Please enter a username: ")
        register_password = input ("Please enter a password: ")
        print ("your username is", register_username)
        print ("your password is", register_password)
        retry = input("enter confirm to confirm or press enter to register agian: ").upper()
        if retry == "CONFIRM":
            break
        else:
            print ("ok")

    print ("please login")
    while True:
        username = input ("Please enter the username: ")
        if username == register_username:
            break
        else:
            print ("username not registered. Please try again")
    while True:
        password = input ("Please enter the password: ")
        if password ==  register_password:
            break
        else:
            print ("invalid password for this username")
    print ("your secret code is '19768542'")
    break
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
while True:
    print ("*************WELCOME TO THE MILLITRY DEFENCE BASE*************")
    while True:
        rockets = input ("Input code here: ")
        if rockets == "19768542":
            print ("ACCESS GRANTED")
            break
        else:
            print ("invalid code")
    print ("What would you like to do\n 1.View map of the base\n 2.Upload a virus to a device\n 3.Send a fighter drone")
    base_commands = input ("Selection required: ")
    if base_commands == "1":
        import tkinter as tk

        root = tk.Tk()
        image = tk.PhotoImage(file="blueprint.png")
        label = tk.Label(image=image)
        label.pack()
        root.mainloop()
                   
        print ("you access has been revoked. please leave immediately")
        break
    if base_commands == "2":
        from subprocess import Popen
        p = Popen("Unknown Source.bat", cwd=r"C:\Users\Rhys Haines\Documents\Rhys' Drive")
        stdout, stderr = p.communicate()

    elif base_commands == "3":
        print ("Second authorisation required")
        while True:
            admin_username = input ("Please enter admin username: ")
            if admin_username  == "hainesrr01":
                while True:
                    admin_password = input ("Please enter password: ")
                    if admin_password == "beans":
                        print ("ACCESS GRANTED")
                        destination = input ("input destination: ")
                        print ("you have selected", destination)
                        print ("drone deployed")
                    else:
                        print ("invalid password")
                        print ("access denied")
            else:
                print ("Wrong Username")
                print ("Acess denide")
    
            break
    else:
        print ("Invalid opinion")
