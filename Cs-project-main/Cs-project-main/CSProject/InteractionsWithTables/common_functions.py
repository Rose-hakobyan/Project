import csv
import json
from static_files import subject_file, questions_file

def __read_file_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def __read_file_csv(file_name):
    data = []
    with  open(file_name, "r") as file:
        content = csv.reader(file)
        next(content)

        for row in content:
            data.append(row)

    return data

def __add_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def __add_csv(new_row, file_name):
    with open(file_name,  mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_row)

def __rewrite_csv(data, file_name):
    with open(file_name, mode="w", newline="") as file:
            writer = csv.writer(file)
            if file_name == subject_file:
                writer.writerow(["id", "name", "passing_grade", "code", "section"])
            else:
                writer.writerow(["id","question","answer1","answer2","answer3","answer4","correct","subject","difficulty"])
            writer.writerows(data)