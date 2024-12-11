from user_code import register
from student_platform import student_platform
from instructor_form import instructor_platform

def register_form():
    while True:
        firstname = None
        lastname = None
        nickname = None
        password = None
        result = None

        while True:
            firstname = input("Insert your firstname: ")
            if firstname != "":
                break
        
        while True:
            lastname = input("Insert your lastname: ")
            if lastname != "":
                break

        while True:
            nickname = input("Insert your nickname: ")
            if nickname != "":
                break

        while True:
            password = input("Insert your password: ")
            if password != "":
                break

        instructor_code = input("Insert instructor code (optional): ")
        
        if instructor_code == "":
            result, message, status = register(nickname, firstname, lastname, password)
        else:
            result, message, status = register(nickname, firstname, lastname, password, "instructor", instructor_code)

        if result:
            if status == "student":
                student_platform(nickname)
            elif status == "instructor":
                instructor_platform(nickname)

        if message == "NicknameFoundError":
            print(f"{nickname} already exists")
        elif message == "NotInstructorError":
            print("Wrong Instructor code")

        while True:
            exit = input("Do you want to exit the registration menu(y/n)? ")
            if exit == "y":
                return
            elif exit == "n":
                break