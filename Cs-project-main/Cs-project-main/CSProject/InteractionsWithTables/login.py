from user_code import login
from student_platform import student_platform
from instructor_form import instructor_platform

def login_form():
    while True:
        nickname = None
        password = None

        while True:
            nickname = input("Insert nickname: ")
            if nickname != "":
                break

        while True:
            password = input("Insert password: ")
            if password != "":
                break

        result, message, status = login(nickname, password)
        
        if result:
            if status == "student":
                student_platform(message)
            elif status == "instructor":
                instructor_platform(message)

        if message == "InccorectPasswordError":
            print("Incorrect Password")
        elif message == "UserNotFoundError":
            print("Nickname does not exist")

        while True:
            exit = input("Do you want to exit the login menu(y/n)?")
            if exit == "y":
                return
            elif exit == "n":
                break