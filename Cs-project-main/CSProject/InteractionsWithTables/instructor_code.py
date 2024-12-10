import user_code as user
import common_functions
import csv
from static_files import subject_file, questions_file

def add_class(name, passing_grade, code, section):
    data = common_functions.__read_file_csv(subject_file)
    id = user.__maximum_id_csv(data)
    
    if not __check_if_class_exists(name, section):
        new_class = [id, name, passing_grade, code, section]
        common_functions.__add_csv(new_class, subject_file)
        return True
    return False

def __check_if_class_exists(name, section):
    data = common_functions.__read_file_json(subject_file)
    for subject in data:
        if subject[1] == name and subject[4] == section:
            return True
        
    return False

def __find_class_by_code(code):
    data = common_functions.__read_file_csv(subject_file)
    for subject in data:
        if subject[3] == code:
            return True
    return False


def __check_if_question_exists(question, subject):
    data = common_functions.__read_file_csv(questions_file)
    for q in data:
        if q[1] == question and q[7] == subject:
            return True
    return False


def __find_question_by_id(question_id):
    questions = common_functions.__read_file_csv(questions_file)
    for question in questions:
        if question[0] == question_id:
            return question
        

def remove_class(subject_id): 
    data = common_functions.__read_file_csv(subject_file)

    updated_data = [row for row in data if int(row[0]) != subject_id]

    if len(updated_data) < len(data):
        common_functions.__rewrite_csv(updated_data, subject_file)
        return True

    return False


def get_classes():
    classes = common_functions.__read_file_csv(subject_file)
    return classes


def get_questions():
    questions = common_functions.__read_file_csv(questions_file)
    return questions

def remove_question(question_id):
    data = common_functions.__read_file_csv(questions_file)
    new_data = [question for question in data if question[0] != str(question_id)]

    if len(new_data) != len(data):
        common_functions.__rewrite_csv(new_data, questions_file)
        return True
    return False


def add_question(question, answers, correct, code, difficulty): #Done
    data = common_functions.__read_file_csv(questions_file)
    id = user.__maximum_id_csv(data)

    if not __check_if_question_exists(question, code) and __find_class_by_code(code):
        new_question = [id, question] + answers + [correct, code, difficulty]
        common_functions.__add_csv(new_question, questions_file)
        return True
    return False


def edit_subject(subject_id, new_name=None, new_section=None, new_passing_grade=None, new_code=None): #Done
    data = common_functions.__read_file_csv(subject_file)
    new_subject = None
    for subject in data:
        if subject[0] == str(subject_id):
            new_subject = subject
            data.remove(subject)
            if new_name:
                new_subject[1] = new_name
            if new_section:
                new_subject[4] = new_section
            if new_passing_grade:
                new_subject[2] = new_passing_grade
            if new_code:
                new_subject[3] = new_code

            data.append(new_subject)
            common_functions.__rewrite_csv(data, subject_file)
            return True
    return False

def edit_question(question_id, question_text=None, a1=None, a2=None, a3=None, a4=None, correct=None, subject=None, difficulty=None):
    questions = common_functions.__read_file_csv(questions_file)
    question = __find_question_by_id(question_id)

    if question:
        questions.remove(question)
        if question_text:
            question[1] = question_text
        if a1:
            question[2] = a1
        if a2:
            question[3] = a2
        if a3:
            question[4] = a3
        if a4:
            question[5] = a4
        if correct:
            question[6] = correct
        if subject:
            if not __find_class_by_code(subject):
                return False, "Class Not Found Error"
            question[7] = subject
        if difficulty:
            question[8] = difficulty

        questions.append(question)
        common_functions.__rewrite_csv(questions, questions_file)
        return True, None
    
    return False, "Question Does Not Exist Error"