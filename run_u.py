users = {}  # Any user can log in if have an account or create an account

Name: "Mchana"
Password: "M1234"

status = "",

while status != "q":
    status = input("Do you have an account? y/n? Press q to quit: ")

    if status == "n":  # new user
        createLogin = input("Create login name: ")

        if createLogin in users:  # check if login name exist in the list
            print ("Login name already exist!\n")
        else:
            createPasswrds = input("Create password: ")
            users[createLogin] = createPasswrds  # add login and password
            print("\nUser created!\n")

    elif status == "y":  # login the user
        login = input("Enter login name: ")

        if login in users:
            passw = input("Enter password: ")
            print ("Welcome")

            if login in users and passw in users:  # login matches password
                print ("Login successful!\n")

        else:
            print
            print("User doesn't exist!\n")
