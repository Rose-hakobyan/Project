# import user_code
# import instructor_code
# import common_functions

# # Define correct paths for MacOS
# subject_file = r"CSProject\Tables\subjects.csv"
# questions_file = r"CSProject\Tables\questions.csv"
# users_file = r"CSProject\Tables\users.json"


# print("Do you want to register or login")
# print("1. Register")
# print("2. Login")
# choice = input("Answer: ")

# if choice == "1":
#     print("\nREGISTRATION")
#     firstname = input("Firstname: ")
#     lastname = input("Lastname: ")
#     nickname = input("Nickname: ")
#     password = input("Password: ")
#     instructor_code = input("Instructor code (optional): ")

#     if user_code.register(nickname, firstname, lastname, password,
#                           status="instructor" if instructor_code == "aua_bocavik" else "student",
#                           instructor_code=instructor_code):
#         print("Registration successful!")
#     else:
#         print("Registration failed.")

# elif choice == "2":
#     print("\nLOGIN")
#     nickname = input("Nickname: ")
#     password = input("Password: ")

#     if user_code.login(nickname, password):
#         users = common_functions.__read_file_json(users_file)
#         subjects = common_functions.__read_file_csv(subject_file)

#         user = next((u for u in users if u["nickname"] == nickname), None)

#         print("\nSubjects:")
#         for i, subject in enumerate(subjects, 1):
#             print(f"{i}. {subject[1]}")

#         subject_idx = int(input("Choose subject: ")) - 1
#         selected_subject = subjects[subject_idx]

#         if user["status"] == "instructor":
#             print(f"\nDetail:")
#             print(f"Name: {selected_subject[1]}")
#             print(f"Code: {selected_subject[3]}")
#             print("\nOperations:")
#             print("1. Add question")
#             print("2. Remove Question")
#             print("3. Modify")

#             op = input("Choose operation: ")

#             if op == "1":
#                 question = input("Question: ")
#                 answer1 = input("Answer 1: ")
#                 answer2 = input("Answer 2: ")
#                 answer3 = input("Answer 3: ")
#                 answer4 = input("Answer 4: ")
#                 correct = input("Correct answer (1-4): ")
#                 print("\nDifficulty:")
#                 print("1. Easy")
#                 print("2. Medium")
#                 print("3. Hard")
#                 difficulty = input("Choose difficulty (1-3): ")

#                 if difficulty == "1":
#                     difficulty = "easy"
#                 elif difficulty == "2":
#                     difficulty = "medium"
#                 elif difficulty == "3":
#                     difficulty = "hard"
#                 else:
#                     print("Invalid difficulty")
#                     exit()

#                 success = instructor_code.add_question(
#                     question=question,
#                     answers=[answer1, answer2, answer3, answer4],
#                     correct=f"Answer {correct}",
#                     subject=selected_subject[3],
#                     difficulty=difficulty
#                 )
#                 print("Question added successfully!" if success else "Failed to add question.")

#             elif op == "2":
#                 questions = common_functions.__read_file_csv(questions_file)
#                 print("\nAvailable questions:")
#                 for q in questions:
#                     if len(q) >= 8 and q[7] == selected_subject[3]:
#                         print(f"ID: {q[0]}, Question: {q[1]}")

#                 question_id = input("\nEnter question ID to remove: ")
#                 success = instructor_code.remove_question(question_id)
#                 print("Question removed successfully!" if success else "Failed to remove question.")

#             elif op == "3":
#                 subject_id = selected_subject[0]
#                 new_name = input("New name (press Enter to keep current): ")
#                 new_section = input("New section (press Enter to keep current): ")
#                 new_passing_grade = input("New passing grade (press Enter to keep current): ")
#                 new_code = input("New code (press Enter to keep current): ")

#                 success = instructor_code.edit_subject(
#                     subject_id,
#                     new_name=new_name if new_name else None,
#                     new_section=new_section if new_section else None,
#                     new_passing_grade=new_passing_grade if new_passing_grade else None,
#                     new_code=new_code if new_code else None
#                 )
#                 print("Subject modified successfully!" if success else "Failed to modify subject.")
#         else:
#             print("\nDifficulty:")
#             print("1. Easy")
#             print("2. Medium")
#             print("3. Hard")

#             diff_choice = input("Choose Difficulty: ")

#             if diff_choice == "1":
#                 difficulty = "easy"
#             elif diff_choice == "2":
#                 difficulty = "medium"
#             elif diff_choice == "3":
#                 difficulty = "hard"
#             else:
#                 print("Invalid difficulty choice")
#                 exit()

#             try:
#                 questions = common_functions.__read_file_csv(questions_file)
#                 test = []
#                 score = 0
#                 total_questions = 0

#                 for q in questions:
#                     if len(q) >= 9 and q[7] == selected_subject[3] and q[8] == difficulty:
#                         test.append(q)

#                 if test:
#                     print("\n=== Quiz Started ===")
#                     for i, q in enumerate(test, 1):
#                         print(f"\nQuestion {i}: {q[1]}")
#                         print(f"1. {q[2]}")
#                         print(f"2. {q[3]}")
#                         print(f"3. {q[4]}")
#                         print(f"4. {q[5]}")

#                         answer = input("\nYour answer (1-4): ")
#                         total_questions += 1

#                         # Extract just the number from the correct answer
#                         correct_num = q[6].replace("Answer ", "")

#                         if answer == correct_num:
#                             score += 1
#                             print("Correct!")
#                         else:
#                             print(f"Wrong! The correct answer was: {correct_num}")

#                     # Display final score
#                     print(f"\nFinal Score: {score}/{total_questions}")

#                 else:
#                     print(f"No questions available for {selected_subject[1]} with {difficulty} difficulty.")
#             except Exception as e:
#                 print(f"Error retrieving questions: {str(e)}")
#     else:
#         print("Login failed!")
# else:
#     print("Invalid choice!")

