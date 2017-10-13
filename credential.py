import sys
import random
import getpass


UserName: "Mchana"
Password: "G1234"
AccountName: "Facebook"
status: ""

n = str("UserName")  # user inputs name
nam = str("")  # users name
a = str("AccountName")  # thas is facebook or any
acc = str("null")
p = str("null")  # user's input start value
pas = str("password")  # password value

ans = True

while ans:
    question = input(
        "Enter a value to get your account: (press enter to quit)")

    answers = random.randint(1, 4)

    if question == "":
        sys.exit()

    elif answers == 1:
        person = input("Enter Name: ")
        print("Valid User", person, '!')

    elif answers == 2:
        holder = input("Account Name: ")
        print("one more step", holder, '!               ')

    elif answers == 3:
        p = getpass.getpass("Insert your password: ")
        print("Welcome!")
