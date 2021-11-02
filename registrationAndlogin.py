from projectoptions import projectOptions

def registeration():
    while True:
        fname = input("please enter firstname :")
        if fname.isalpha():
            break

    while True:
        lname = input("please enter lastname :")
        if lname.isalpha():
            break

    email = input("please enter email :")
    while "@" not in email:
        email = input('please enter email :')
        if "." not in email:
            email = input('please enter email :')

    while True:
        password = input("please enter password :")
        if password.isdigit():
            break

    while True:
        c_password = input("please confirm password :")
        c_password.isdigit()
        if c_password == password:
            break

    while True:
        phone = input("please enter phone number :")
        if phone.isdigit():
            break

    datalist = ",".join([fname, lname, email, password, phone])
    datalist = datalist + "\n"
    try:
        readfile = open("users.txt")
    except:
        print("file not found")
    else:
        data = readfile.readlines()
        users = []
        for item in data:
            users.append(item.strip("\n"))
        for user in users:
            userdetails = user.split(",")
            if userdetails[2] == email:
                print("## user already exist register again pick another email ##")
                readfile.close()
                registeration()
        else:
            readfile.close()
            try:
                file = open("users.txt", "a")
            except:
                print("file not found")
            else:
                file.write(datalist)
                file.close()
                print("## registration successfully ##")

def login():
    email = input("please enter email :")
    while "@" not in email:
        email = input('please enter email :')
        if "." not in email:
            email = input('please enter email :')

    while True:
        password = input("please enter password :")
        if password.isdigit():
            break


    readfile = open("users.txt")
    data = readfile.readlines()
    users = []
    for item in data:
        users.append(item.strip("\n"))
    for user in users:
        userdetails = user.split(",")
        if userdetails[2] == email and userdetails[3] == password:
            print("## logged in successfully ##")
            readfile.close()
            projectOptions(email)
            break
    else:
        print("## invalid user login again ##")
        login()




