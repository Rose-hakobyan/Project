import common_functions
import random 
import user_code
from static_files import  subject_file, questions_file, users_file

__cache = []
__pass_grade = None
__class = None
__nickname = None

# Internal Functions
def __find_class(class_code):
    subjects = common_functions.__read_file_csv(subject_file)

    for subject in subjects:
        if subject[3] == class_code:
            return subject
        
def __find_questions(class_code):
    data = common_functions.__read_file_csv(questions_file)
    needed_questions = []
    for row in data:
        if row and row[7] == class_code:
            needed_questions.append(row)

    return needed_questions

def __sort_questions(class_code):
    questions = __find_questions(class_code)
    easy = []
    medium = []
    hard = []
    for question in questions:
        if question[8] == "easy":
            easy.append(question)
        if question[8] == "medium":
            medium.append(question)
        if question[8] == "hard":
            hard.append(question)
    return [easy, medium, hard]


def __generate_test(class_code, easy_count, medium_count, hard_count):
    global __cache
    questions = __sort_questions(class_code)
    easy = questions[0]
    medium = questions[1]
    hard = questions[2]

    new_quiz = []

    for i in range(easy_count):
        number = random.randint(0, len(easy) - 1)
        new_quiz.append(easy[number])
        easy.remove(easy[number])

    for i in range(medium_count):
        number = random.randint(0, len(medium) - 1)
        new_quiz.append(medium[number])
        medium.remove(medium[number])

    for i in range(hard_count):
        number = random.randint(0, len(hard) - 1)
        new_quiz.append(hard[number])
        hard.remove(hard[number])

    student_version = []
    __cache = new_quiz

    for i in new_quiz:
        student_version.append([
            i[1],
            i[2],
            i[3],
            i[4],
            i[5]
        ])

    return student_version

def __add_grade(grade_data):
    global __nickname
    student = user_code.__find_by_nickname(__nickname)
    grades = student.get("grades")
    grades.append(grade_data)
    user_code.modify(__nickname, grades=student["grades"])


# External Functions
def get_test(nickname, class_code, difficulty):
    global __cache, __nickname, __pass_grade, __class

    subject = __find_class(class_code)
    if subject:
        __pass_grade  = int(subject[2])
        __class = subject[1]
        __cache = None
        __nickname = nickname

        quiz = []
        if difficulty == "easy":
            quiz = __generate_test(class_code, 5, 4, 1)
        if difficulty == "medium":
            quiz = __generate_test(class_code, 4, 4, 2)
        if difficulty == "hard":
            quiz = __generate_test(class_code, 3, 3, 4)

        return quiz

def grade_quiz(student_answers):
    global __cache, __pass_grade, __class
    correct = 0
    correct_answers = [i[6] for i in __cache]

    for i in range(len(student_answers)):
        if student_answers[i] == correct_answers[i]:
            correct += 1

    score = correct * 10
    is_passed = "Passed!" if score >= __pass_grade else "Failed!"

    grade_data =  {__class : [score, is_passed]}

    __add_grade(grade_data)

    return score, is_passed

def classes():
    all_classes = common_functions.__read_file_csv(subject_file)
    return all_classes

def get_grades(nickname):
    student = user_code.__find_by_nickname(nickname)

    return student["grades"]