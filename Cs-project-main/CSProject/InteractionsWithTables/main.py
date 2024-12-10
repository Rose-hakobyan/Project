from register import register_form
from login import login_form

def main_menu():
    
    while True:
        print("Welcome to the Quiz Game! Register or Login to continue")
        print("1. Register")
        print("2. Login")
        answer = int(input("Insert 1 or 2: "))
        if answer == 1:
            register_form()
        if answer == 2:
            login_form()

        while True:
            exit = input("Do you want to exit main menu(y/n)? ")
            if exit == "y":
                return
            elif exit == "n":
                break

if __name__ == "__main__":
    main_menu()