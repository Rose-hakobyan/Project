from student_code import classes, get_grades, get_test, grade_quiz
from user_code import modify

__nickname = None

def __print_classes():
    available_classes = classes()
    print("==== ALL CLASSES ====")
    for current_class in available_classes:
        print("=================")
        print(f"Class: {current_class[1]}")
        print(f"class code: {current_class[3]}")
        print(f"Passing grade: {current_class[2]}")
        print(f"Section: {current_class[4]}")


def __print_grades():
    grades = get_grades(__nickname)

    print("==== MY GRADES ====")
    for grade in grades:
        print("=================")
        for key, values in grade.items():
            print(key)
            print(f"grade:  {values[0]}")
            print(f"Result: {values[1]}")


def __take_new_test():
    while True:
        generated_test = None

        __print_classes()
        class_code = input("Insert the code of the class: ")
        
        print("Available difficulties")
        print("1. easy")
        print("2. medium")
        print("3. hard")
        
        while True:
            difficulty = input("Insert 1, 2 or 3: ")
            
            if difficulty == "1":
                generated_test = get_test(__nickname, class_code, "easy")
                break
            if difficulty == "2":
                generated_test = get_test(__nickname, class_code, "medium")
                break
            if difficulty == "3":
                generated_test = get_test(__nickname, class_code, "hard")
                break
            else:
                print("Incorrect input")
        
        if generated_test:
            print("==== NEW QUIZ ====")
            __start_test(generated_test)
            break

        print("Incorrect class code")


def __start_test(test):
    student_answers = []
    number = 1

    for question in test:
        print("=================")
        print(f"QUESTION {number}")
        print(question[0])
        print("Variants: ")
        print(f"1) {question[1]}    2) {question[2]}    3) {question[3]}    4) {question[4]}")

        while True:
            answer = input("Insert your answer [1, 4]: ")
            
            if answer == "1" or answer == "2" or answer == "3" or answer == "4":
                student_answers.append(f"answer{answer}")
                break
            print("Incorrect format")

        number += 1

    score, is_passed = grade_quiz(student_answers)

    print(f"You {is_passed} with score {score}")

def __edit_profile():
    print("==== EDIT PROFILE ====")
    print("Just press [enter] if you don't want to change the field")
    firstname = input("firstname: ")
    lastname = input("lastname:  ")
    password = input("password")
   
    if firstname == "":
        firstname = None
    if lastname == "":
        lastname = None
    if password == "":
        password = None

    modify(__nickname, firstname=firstname, lastname=lastname, password=password)
    print("Account modified successfully")


def student_platform(nickname):
    global __nickname
    __nickname = nickname
    while True:
        print("==== STUDENT PLATFORM ====")
        print("Choose where to go")
        print("1. Take a new test")
        print("2. My Grades")
        print("3. Modify")
        print("4. Log Out")

        answer = input("Insert 1, 2, 3 or 4: ")

        if answer == "1":
            __take_new_test()
        if answer == "2":
            __print_grades()
        if answer == "3":
            __edit_profile()
        if answer == "4":
            break
        else:
            print("Incorrect input")