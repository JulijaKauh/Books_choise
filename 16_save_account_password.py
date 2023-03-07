#!/usr/bin/env python3
def view():
    with open("password.txt", "r") as file:
        for line in file:
            data = line.strip()
            account, password = data.split(":")
            print("Account: ", account, "|| password: ", password)
            

def add():
    account = input("Enter your account: ")
    password = input("Enter you pasword: ")
    with open("password.txt", "a") as file:
        file.write(account + ":" + password + "\n")

while True:
    mode = input("View existing passwords or add a new password, or q to quit: ").lower()

    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
