from instructor_code import add_class, add_question, get_classes, remove_class, get_questions, remove_question, edit_subject, edit_question
from user_code import modify

__nickname = None

def __add_class():
    while True:
        print("==== NEW CLASS FORM ====")
        
        name = input("Insert name: ")
        
        while True:
            passing_grade = input("Insert passing grade (10-100): ")
            if int(passing_grade) < 10 or int(passing_grade) > 100:
                print("Incorrect input")
            else:
                break

        while True:
            code = input("Insert code in format XX000: ")
            if len(code) == 7 and code[:4].isalpha() and code[4:].isdigit():
                break
            if len(code) == 5 and code[:2].isalpha() and code[2:].isdigit():
                break
            print("Incorrect input")
        
        while True:
            section = input("Insert section: ").upper()
            if section.isalpha():
                break
            print("Incorrect input")

        if add_class(name, passing_grade, code, section):
            print("class added successfully")
        else:
            print("The class already exists")
        
        while True:
            again = input("Do you want to add another class(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


def __add_question():
    while True:
        print("==== NEW QUESTION FORM ====")
        
        question = input("Insert your question: ")

        a1 = input("Insert answer 1: ")
        a2 = input("Insert answer 2: ")
        a3 = input("Insert answer 3: ")
        a4 = input("Insert answer 4: ")

        while True:
            correct_answer = input("Insert correct answer: ")
            if correct_answer == "1" or correct_answer == "2" or correct_answer == "3" or correct_answer == "4":
                correct_answer = f"answer{correct_answer}"
                break

        while True:
            code = input("Insert code in format XX(XX)000: ")
            if len(code) == 7 and code[:4].isalpha() and code[4:].isdigit():
                break
            if len(code) == 5 and code[:2].isalpha() and code[2:].isdigit():
                break
            print("Incorrect input")

        while True:
            print("Choose difficulty")
            print("1. easy")
            print("2. medium")
            print("3. hard")
            difficulty = input("Insert 1, 2 or 3: ")

            if difficulty == "1":
                difficulty = "easy"
                break
            if difficulty == "2":
                difficulty == "medium"
                break
            if difficulty == "3":
                difficulty = "hard"
                break

            print("Incorrect input")
        
        if add_question(question, [a1, a2, a3, a4], correct_answer, code, difficulty):
            print("Question added successfully")
        else:
            print("Question already exists")

        while True:
            again = input("Do you want to add another question(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


def __remove_class():
    while True:
        print("==== REMOVE AN EXISTING CLASS ====")
        classes = get_classes()

        for subject in classes:
            print(f"id: {subject[0]} | name: {subject[1]} | section: {subject[4]}")

        subject_id = input("Insert id: ")

        if remove_class(int(subject_id)):
            print("Class removed successfully")
        else:
            print("Id incorrect")

        while True:
            again = input("Do you want to remove another class(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


def __remove_question():
    while True:
        print("==== REMOVE AN EXISTING QUESTION ====")
        questions = get_questions()

        for question in questions:
            print(f"id: {question[0]} | question: {question[1]} | subject: {question[7]}")

        question_id = input("Insert id: ")
        if remove_question(question_id):
            print("Question removed successfully")
        else:
            print("Question does not exist")

        while True:
            again = input("Do you want to remove another question(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


def __edit_class():
    while True:
        print("==== EDIT CLASS ====")
        classes = get_classes()

        for subject in classes:
            print(f"id: {subject[0]} | name: {subject[1]} | passing grade: {subject[2]} | code: {subject[3]} | section: {subject[4]}")

        print("===============================")
        
        subject_id = input("Insert subject id: ")
        print("Just miss the fields that don't require changes")

        name = input("Insert name: ")

        while True:
            passing_grade = input("Insert passing grade (10-100): ")
            if passing_grade == "":
                break
            if int(passing_grade) < 10 or int(passing_grade) > 100:
                print("Incorrect input")
            else:
                break

        while True:
            code = input("Insert code in format XX(XX)000: ")
            if code == "":
                break
            if len(code) == 7 and code[:4].isalpha() and code[4:].isdigit():
                break
            if len(code) == 5 and code[:2].isalpha() and code[2:].isdigit():
                break
            print("Incorrect input")
        
        while True:
            section = input("Insert section: ").upper()
            if section == "":
                break
            if section.isalpha():
                break
            print("Incorrect input")

        if edit_subject(subject_id, name, section, passing_grade, code):
            print("Class data changed successfully")
        else:
            print("Something went wrong or the class does not exist")

        while True:
            again = input("Do you want to edit another class(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


def __edit_question():
    while True:
        print("==== EDIT QUESTION ====")
        questions = get_questions()

        for question in questions:
            print("====================")
            print(f"id: {question[0]}")
            print(f"question: {question[1]}")
            print("Answers:")
            print(f"1) {question[2]}    2) {question[3]}    3) {question[4]}    4) {question[5]}")
            print(f"correct answer: {question[6]}")
            print(f"Class code: {question[7]}")
            print(f"Difficulty: {question[8]}")

        print("====================")
        question_id = input("Insert question id: ")
        print("Just miss the fields that don't require changes")

        question = input("Insert question: ")
        a1 = input("Insert answer 1: ")
        a2 = input("Insert answer 2: ")
        a3 = input("Insert answer 3: ")
        a4 = input("Insert answer 4: ")
        while True:
            possible = ["1", "2", "3", "4"]
            correct = input("Insert correct answer [1, 4]: ")
            if correct == "":
                break
            if correct in possible:
                correct = f"answer{correct}"
        class_code = input("Insert class code: ")
        difficulty = input("Insert difficulty: ")

        if question == "":
            question = None
        if a1 == "":
            a1 = None
        if a2 == "":
            a2 = None
        if a3 == "":
            a3 = None
        if a4 == "":
            a4 = None
        if correct == "":
            correct = None
        if correct == "":
            correct = None
        if class_code == "":
            class_code = None
        if difficulty == "":
            difficulty = None

        result, message = edit_question(question_id, question, a1, a2, a3, a4, correct, class_code, difficulty)
        if result:
            print("Question edited successfully")
        else:
            print(message)

        while True:
            again = input("Do you want to edit another question(y/n)? ")
            if again == "y":
                break
            if again == "n":
                return


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



def instructor_platform(nickname):
    global __nickname
    __nickname = nickname
    while True:
        print("==== INSTRUCTOR PLATFORM ====")
        print("Choose where to go")
        print("1. Add class")
        print("2. Add question")
        print("3. Remove class")
        print("4. Remove question")
        print("5. Edit class")
        print("6. Edit question")
        print("7. Modify")
        print("8. Log out")

        answer = input("Insert number [1, 8]: ")

        if answer == "1":
            __add_class()
        if answer == "2":
            __add_question()
        if answer == "3":
            __remove_class()
        if answer == "4":
            __remove_question()
        if answer == "5":
            __edit_class()
        if answer == "6":
            __edit_question()
        if answer == "7":
            __edit_profile()
        if answer == "8":
            break