import hashlib
import common_functions
from static_files import users_file

#Internal functions
def __find_by_nickname(nickname):
    data = common_functions.__read_file_json(users_file)
    for user in data:
        if user["nickname"] == nickname:
            return user
        
    return
    
def __maximum_id_json(data):
    maximum = 0
    for user in data:
        if user["id"] > maximum:
            maximum = user["id"]

    return maximum + 1

def __maximum_id_csv(data):
    maximum = 0
    for user in data:
        if int(user[0]) > maximum:
            maximum = int(user[0])

    return maximum + 1


def __hash_password(password):
    password_bytes = password.encode('utf-8')
    
    hash_object = hashlib.sha256()
    
    hash_object.update(password_bytes)
    
    hashed_password = hash_object.hexdigest()
    
    return hashed_password


def __check_if_instructor(instructor_code):
    return instructor_code == "aua_bocavik"        

#External Functions
def modify(nickname, firstname = None, lastname = None, password = None, grades = None, questions = None):
    data = common_functions.__read_file_json(users_file)
    user = __find_by_nickname(nickname)

    if user:
        data.remove(user)
        
        if firstname:
            user["firstname"] = firstname
        if lastname:
            user["lastname"] = lastname
        if password:
            new_password = __hash_password(password)
            user["password"] = new_password
        if grades:
            user["grades"] = grades
        if questions:
            user["questions"] = questions

        data.append(user)
        common_functions.__add_json(data, users_file)


def register(nickname, firstname, lastname, password, status = "student", instructor_code = None):
    data = common_functions.__read_file_json(users_file)
    if __find_by_nickname(nickname):
        return False, "NicknameFoundError", None
    
    if instructor_code and not __check_if_instructor(instructor_code):
        return False, "NotInstructorError", None
    
    id = __maximum_id_json(data)
    password = __hash_password(password)
    new_user = {
        "id": id, 
        "nickname":nickname, 
        "firstname":firstname, 
        "lastname":lastname, 
        "status":status, 
        "grades":[],
        "password":password,
        }

    
    data.append(new_user)
    common_functions.__add_json(data, users_file)

    return True, nickname, status


def login(nickname, password):
    data = common_functions.__read_file_json(users_file)
    current_user = __find_by_nickname(nickname)
    if not current_user:
        return False, "UserNotFoundError", None
    
    current_password = __hash_password(password)
    original_password = current_user["password"] 
    
    if current_password == original_password:
        nickname = current_user["nickname"]
        return True, nickname, current_user["status"]

    return False, "InccorectPasswordError", None

def remove(nickname):
    data = common_functions.__read_file_json(users_file)
    current_user = __find_by_nickname(nickname)

    if not current_user:
        return False
    
    data.remove(current_user)

    common_functions.__add_json(data, users_file)

    return True