from registrationAndlogin import registeration, login

while True:
    choice = input("please write l for login , r for registeration or e for exit : ")
    choice = choice.strip()
    if choice.isalpha():
        if choice == "r":
            registeration()
        elif choice == "l":
            login()
        elif choice == "e":
            exit()
