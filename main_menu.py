import datetime
from datetime import *
import random

# START OF ADMINISTRATOR AND MAIN MENU MODULE


def check_backup_date():  # Checks if the difference between the last backup and today is 3 days
    backup_filepath = "../files/backup_date.txt"
    try:
        with open(backup_filepath, "r") as file:
            last_backup_date = datetime.strptime(file.readline(), '%d-%m-%y').date()
            if datetime.today().date() - last_backup_date > timedelta(days=3):  # Only back up data every 3 days
                autobackup()
    except FileNotFoundError:
        print("Backup Failed! File not found. Contact developer.")


def autobackup():  # Copies the contents of the files in /files directory and create a copy in the backup_files directory
    all_files = ["accountants", "admins", "courses", "faculty", "fees", "grades", "lecturers", "modules", "registrars", "students"]
    filepath = "../files/"
    backup_filepath = "../backup_files/"
    try:
        for file in all_files:
            path = f"{filepath}{file}.txt"
            backup_path = f"{backup_filepath}{file}.txt"
            with open(path, "r") as f:
                file_contents = f.readlines()
            with open(backup_path, "w") as other_file:
                other_file.writelines(file_contents)

        print("Backup successful! Last backup date has been updated.")
        update_backup_date()
    except FileNotFoundError:
        print("Backup Failed! File not found. Contact developer.")


def update_backup_date():  # Updates the backup_date.txt with the current date.
    backup_filepath = "../files/backup_date.txt"
    try:
        with open(backup_filepath, "w") as file:
            current_date = str(datetime.now().strftime('%d-%m-%y'))
            file.writelines(current_date)
    except FileNotFoundError:
        print("Backup Success, but Date not Updated! File not found. Contact developer.")


def check_backup_date_file():  # Checks if backup_date.txt exists, if no, it creates a new file
    backup_filepath = "../files/backup_date.txt"
    try:
        file = open(backup_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(backup_filepath, "x")
        file.write(str(datetime.now().strftime('%d-%m-%y')))
        file.close()


def check_courses_file():  # Checks if courses.txt exists, if no, it creates a new file
    courses_filepath = "../files/courses.txt"
    try:
        file = open(courses_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(courses_filepath, "x")
        file.close()


def check_faculties_file():  # Checks if faculty.txt exists, if no, it creates a new file
    faculty_filepath = "../files/faculty.txt"
    try:
        file = open(faculty_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(faculty_filepath, "x")
        file.close()


def check_admin_file():  # Checks if admins.txt exists, if no, it creates a new file
    admin_filepath = "../files/admins.txt"
    try:
        file = open(admin_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(admin_filepath, "x")

        print("")
        print("It seems like this is the first time running this program! Let's set up an admin account.")
        print("")
        print("==============")
        print("Create Account")
        print("==============")

        admin_id = ""
        while True:
            try:
                if len(admin_id) < 4:
                    admin_id = input("Username (min. 4 characters): ")
                else:
                    break
            except ValueError:
                pass

        admin_password = ""
        while True:
            try:
                if len(admin_password) < 7:
                    admin_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        file.write(f"{admin_id},{admin_password}")

        print("Administrator account set up successfully!")
        print("")

        file.close()


def check_registrar_file():  # Checks if registrars.txt exists, if no, it creates a new file
    registrar_filepath = "../files/registrars.txt"
    try:
        file = open(registrar_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(registrar_filepath, "x")
        file.close()


def check_accountant_file():  # Checks if accountants.txt exists, if no, it creates a new file
    accountant_filepath = "../files/accountants.txt"
    try:
        file = open(accountant_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(accountant_filepath, "x")
        file.close()


def check_students_file():  # Checks if students.txt exists, if no, it creates a new file
    students_filepath = "../files/students.txt"
    try:
        file = open(students_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(students_filepath, "x")
        file.close()


def check_lecturers_file():  # Checks if students.txt exists, if no, it creates a new file
    lecturers_filepath = "../files/lecturers.txt"
    try:
        file = open(lecturers_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(lecturers_filepath, "x")
        file.close()


def check_modules_file():  # Checks if modules.txt exists, if no, it creates a new file
    modules_filepath = "../files/modules.txt"
    try:
        file = open(modules_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(modules_filepath, "x")
        file.close()


def check_fees_files():  # Checks if fees.txt exists, if no, it creates a new file
    fees_filepath = "../files/fees.txt"
    try:
        file = open(fees_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(fees_filepath, "x")
        file.close()


def check_grades_file():  # Checks if grades.txt exists, if no, it creates a new file
    grades_filepath = "../files/grades.txt"
    try:
        file = open(grades_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(grades_filepath, "x")
        file.close()


def check_lecturer_account_file():  # Checks if lecturer_accounts.txt exists, if no, it creates a new file
    lecturer_account_filepath = "../files/lecturer_accounts.txt"
    try:
        file = open(lecturer_account_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(lecturer_account_filepath, "x")
        file.close()


def check_student_account_file():  # Checks if lecturer_accounts.txt exists, if no, it creates a new file
    student_account_filepath = "../files/student_accounts.txt"
    try:
        file = open(student_account_filepath, "r")
        file.close()
    except FileNotFoundError:
        file = open(student_account_filepath, "x")
        file.close()


def login_admin():  # The login page for admins
    print("")
    print("========================")
    print("Administrator Login Page")
    print("========================")

    admin_id = ""
    while True:
        if len(admin_id) < 4:  # Length check for the admin username
            admin_id = input("Username (min. 4 characters): ")
        else:
            break

    admin_password = ""
    while True:
        if len(admin_password) < 7:  # Length check for the admin password
            admin_password = input("Password (min. 7 characters): ")
        else:
            break

    check_admin_login(admin_id, admin_password)  # Sends the username and password to check_admin_login()


def check_admin_login(user_id, user_password):  # Checks if the username and password provided exists and matches
    admin_filepath = "../files/admins.txt"  # Relative filepath for the collection of admin usernames and passwords
    registered_admin_usernames = []
    registered_admin_passwords = []

    try:
        with open(admin_filepath, "r") as file:
            accounts = file.readlines()  # Fetches all admin accounts stored
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    for account in accounts:
        username, password = account.strip('\n').split(",")
        registered_admin_usernames.append(username)
        registered_admin_passwords.append(password)
    if user_id in registered_admin_usernames:
        if user_password == registered_admin_passwords[registered_admin_usernames.index(user_id)]:
            print("")
            print("Admin login successful!")
            print("")

            admin_menu()
        else:
            admin_login_fail()
    else:
        admin_login_fail()


def admin_login_fail():  # Gives the user options to try again or to choose their account type again.
    print("")
    print("The username/password you enter is incorrect! Would you like to:")
    print("1) Try again")
    print("2) Return to main menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2): "))  # Gets the user's input
            if choice in [1, 2]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 2!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 2!")
            print("")

    match choice:
        case 1:
            login_admin()  # Re-displays the admin login page
        case 2:
            main_menu()  # Sends user to the main menu


def is_page_full(pages):  # Checks if a 'page' is full (max. 5)
    length = len(pages)
    if len(pages[length]) < 5:
        return False
    return True


def create_new_page(pages):  # Used together with is_page_full(). If page is full, a new one is created
    length = len(pages)
    pages[length + 1] = []


def write_to_page(pages, entry):  # Adds an entry to a page
    length = len(pages)
    pages[length].append(entry)


def admin_menu():  # The admin main menu
    print("======================")
    print("Admin Menu")
    print("======================")
    print("1) Manage Courses")
    print("2) Manage Students")
    print("3) Manage Lecturers")
    print("4) Manage Faculties")
    print("5) Manage Modules")
    print("6) Generate Report")
    print("7) View All Data")
    print("8) Register an Account")
    print("9) Log Out")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6/7/8/9): "))  # Gets the user's input
            if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 9!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 9!")
            print("")

    match choice:
        case 1:
            manage_courses_menu()
        case 2:
            manage_students_menu()
        case 3:
            manage_lecturers_menu()
        case 4:
            manage_faculties_menu()
        case 5:
            manage_modules_menu()
        case 6:
            generate_report()
        case 7:
            view_all_data()
        case 8:
            account_registration_menu()
        case 9:
            admin_logout()


def manage_courses_menu():  # Menu for everything related to courses
    print("======================")
    print("Course Management Menu")
    print("======================")
    print("1) Add A Course")
    print("2) Remove A Course")
    print("3) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3): "))  # Gets the user's input
            if choice in [1, 2, 3]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 3!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 3!")
            print("")

    match choice:
        case 1:
            add_course()
        case 2:
            delete_course()
        case 3:
            admin_menu()


def add_course():  # Creates a new course and stores it to file
    courses_filepath = "../files/courses.txt"  # Relative filepath for the collection courses
    print("============")
    print("Add A Course")
    print("============")
    print("")

    try:
        with open(courses_filepath, "r") as file:  # Reads the courses.txt file
            courses = file.readlines()  # Gets all the current courses
            used_course_codes = []
            for course in courses:
                used_course_codes.append(course[0:5])  # Gets all the course codes that have been used

            course_code = ""
            while True:
                try:
                    if len(course_code) != 5 or course_code in used_course_codes:  # Length and uniqueness check for course code
                        if len(used_course_codes) == 0:  # If there are no existing courses, no additional info is shown
                            pass
                        else:  # Shows the last used course code
                            print(f"Last Used Course Code: {used_course_codes[len(used_course_codes) - 1]}")
                        course_code = input("Course Code (5 characters and unique): ")
                    else:
                        break
                except ValueError:
                    pass

            course_name = input("Course Name: ")

            while True:
                try:
                    course_credits = int(input("Course Credits: "))
                    if course_credits < 1:  # Course credits cannot be 0
                        print("You need to enter an integer value larger than 0!")
                    else:
                        break
                except ValueError:
                    print("You need to enter an integer value!")
                    print("")

            while True:
                try:
                    course_fees = int(input("Enter Course Fees: "))
                    if course_fees > 0:
                        break
                    else:
                        print("You need to enter an integer value larger than 0!")
                        print("")
                except ValueError:
                    print("You need to enter an integer value!")

    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(courses_filepath, "a") as file:
            if used_course_codes:
                entry = f"\n{course_code},{course_name},{course_credits},{course_fees}"  # Compiles the info above into the format: course_code,course_name, course_credits
            else:
                entry = f"{course_code},{course_name},{course_credits},{course_fees}"
            file.write(entry)  # Writes the info to file

            print("")
            print("Course has been created successfully!")
            print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    manage_courses_menu()  # Brings the user back to the course menu


def delete_course():  # Removes an existing course from the file
    courses_filepath = "../files/courses.txt"  # Relative filepath for the collection courses
    try:
        with open(courses_filepath, "r") as file:  # Opens file in read mode
            courses = file.readlines()
            available_course_codes = []
            for course in courses:  # Gets all the existing course codes that can be deleted
                available_course_codes.append(course[0:5])

        if len(available_course_codes) == 0:  # If there are no courses, user cannot delete anything
            print("")
            print("There are no courses yet! You need to create a course before deleting one.")
            print("")
            manage_courses_menu()

        target_course_code = ""  # Gets the course code that the user wants to delete
        while True:
            try:
                if len(target_course_code) != 5 or target_course_code not in available_course_codes:  # Length and existence check
                    if target_course_code == 'exit':  # Option for user to cancel the deletion process
                        manage_courses_menu()
                    else:
                        print(
                            f"The latest course code in use is {available_course_codes[len(available_course_codes) - 1]}")  # Shows the latest course code
                        print("Enter 'exit' to return to previous menu.")
                        target_course_code = input("Course Code (5 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        if len(courses) == 1:  # If there is only one student registered, do not need to search for student, just delete everything straightaway
            open(courses_filepath, 'w').close()
            print(f"Course {target_course_code} was successfully deleted!")
            print("")
            manage_students_menu()
        else:
            for course in courses:
                if target_course_code == course[0:5]:  # Searches through the array and pops the intended course
                    courses.pop()
            try:
                with open(courses_filepath, "w") as file:
                    file.writelines(courses)  # Overwrites the current file with the new collection of courses
                print(f"Course {target_course_code} was successfully deleted!")
                print("")
                manage_courses_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_courses():  # Lists all courses in paginated view
    courses_filepath = "../files/courses.txt"  # Relative filepath of the collection of courses
    pages = {1: []}  # Initializes a dictionary that stores pages

    try:
        with open(courses_filepath, "r") as file:  # Reads and gets the courses from the file
            courses = file.readlines()

            for course in courses:
                course = course.strip('\n')
                if is_page_full(pages):  # Check if the current page is full
                    create_new_page(pages)  # If yes, create a new page
                write_to_page(pages, course)  # Writes each course to the latest available page

            print(f"There are {len(courses)} courses registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(
                        f"Page {page} (First Entry: {pages.get(page)[0][0:5]})")  # Shows the course code of the first course in each page
                while True:
                    try:
                        print("")
                        target_page = int(input("Enter the desired page number (Enter 0 to exit): "))
                        if type(target_page) is int and 0 <= target_page <= len(pages):
                            if target_page == 0:  # Exit option for user
                                print("")
                                view_all_data()
                            break
                    except ValueError:
                        pass
                if target_page > len(pages):  # Checks if page exists
                    print(f"Page {target_page} does not exist!")
                else:
                    current_courses = pages.get(target_page)  # Prints all courses stored on that page
                    for course in current_courses:
                        course_code, course_name, course_credits, course_fees = course.split(',')
                        print(f"Course Code: {course_code}")
                        print(f"Course Name: {course_name}")
                        print(f"Course Credits: {course_credits}")
                        print(f"Course Fees: ${course_fees}")
                        print("=====================================")


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def manage_students_menu():  # Menu with everything related to students
    print("======================")
    print("Student Management Menu")
    print("======================")
    print("1) Edit Student Data")
    print("2) Remove Student Data")
    print("3) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3): "))  # Gets the user's input
            if choice in [1, 2, 3]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 3!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 3!")
            print("")

    match choice:
        case 1:
            edit_student()
        case 2:
            delete_student()
        case 3:
            admin_menu()


def edit_student():
    target_student = ""
    students_filepath = "../files/students.txt"  # Relative filepath for the collection of students stored
    available_student_ids = []

    try:
        with open(students_filepath, 'r') as file:  # Reads and fetches all student data stored
            students = file.readlines()
            for student in students:
                student_id = student[0:5]  # Gets student IDs and add them to list
                available_student_ids.append(student_id)

        if len(available_student_ids) == 0:
            print("")
            print("There are no students to edit!")
            manage_students_menu()
        else:
            target_student_id = ""  # Gets the target student ID from user
            while True:
                try:
                    if len(target_student_id) != 5 or target_student_id not in available_student_ids:  # Length and existence check
                        if target_student_id == 'exit':  # Exit option for users
                            manage_students_menu()
                        if len(available_student_ids) == 0:  # Check if there are students at all
                            print("")
                            print("There are no students yet! A registrar account needs to create a student account first.")
                            print("")
                            manage_students_menu()
                        else:
                            print(
                                f"The latest student ID in use is {available_student_ids[len(available_student_ids) - 1]}")  # Shows the latest student ID
                            print("Enter 'exit' to return to previous menu.")
                            target_student_id = input("Student ID (5 characters and exists): ")
                    else:
                        break
                except ValueError:
                    pass

            for student in students:  # Searches for the data of the intended student
                if student[0:5] == target_student_id:
                    target_student = student

            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(',')

            print("============================")  # Displays the current student info
            print(f"Student ID: {current_student_id}")
            print(f"Student Name: {current_name}")
            print(f"Student Course: {current_course_code}")
            print(f"Student Phone Number: {current_phone_number}")
            print(f"Student Email: {current_email}")
            print(f"Student Gender: {current_gender}")
            print(f"Student Date of Birth: {current_dob}")
            print("============================")

            print("")
            print("What do you wish to edit?")
            print("")
            print("1) Student Name")
            print("2) Student Course")
            print("3) Student Phone Number")
            print("4) Student Email")
            print("5) Student Gender")
            print("6) Student Date of Birth")
            print("7) Return to student menu")
            print("")

            while True:  # Repeats infinitely unless a valid choice is given
                try:
                    choice = int(input("Enter your choice (1/2/3/4/5/6/7): "))  # Gets the user's input
                    if choice in [1, 2, 3, 4, 5, 6, 7]:  # Checks if the user input is valid
                        break  # Stops the while loop
                    else:
                        print("You need to enter a value between 1 and 7!")
                        print("")
                except ValueError:  # Exception handling in case a non-integer value is inputted
                    print("You need to enter a value between 1 and 7!")
                    print("")

            match choice:
                case 1:
                    change_student_name(target_student_id, students, current_name)
                case 2:
                    change_student_course(target_student_id, students, current_course_code)
                case 3:
                    change_student_phone_number(target_student_id, students, current_phone_number)
                case 4:
                    change_student_email(target_student_id, students, current_email)
                case 5:
                    change_student_gender(target_student_id, students, current_gender)
                case 6:
                    change_student_dob(target_student_id, students, current_dob)
                case 7:
                    manage_students_menu()

    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def delete_student():  # Searches for a student ID and pops it from the array
    students_filepath = "../files/students.txt"  # Relative filepath of collection of student data
    try:
        with open(students_filepath, "r") as file:  # Reads and fetches student data
            students = file.readlines()
            available_student_ids = []
            for student in students:
                available_student_ids.append(student[0:5])

        target_student_id = ""
        while True:  # Infinitely asks for student ID until valid ID is given
            try:
                if len(target_student_id) != 5 or target_student_id not in available_student_ids:  # Length and existence check
                    if target_student_id == 'exit':  # Exit option for users
                        manage_courses_menu()
                    if len(available_student_ids) == 0:  # If there are no students, do not allow user to delete anything
                        print("")
                        print("There are no students registered yet! A registrar needs to register a student before deleting one.")
                        print("")
                        manage_students_menu()
                    else:
                        print(f"The latest student ID in use is {available_student_ids[len(available_student_ids) - 1]}")  # Shows the last registered student ID
                        print("Enter 'exit' to return to previous menu.")
                        target_student_id = input("Student ID (5 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        if len(students) == 1:  # If there is only one student registered, do not need to search for student, just delete everything straightaway
            open(students_filepath, 'w').close()
            print(f"Student {target_student_id} was successfully deleted!")
            print("")
            manage_students_menu()
        else:
            for student in students:
                if target_student_id == student[0:5]:
                    students.pop(students.index(student))  # Get the index of the matching student and pops it
            try:
                with open(students_filepath, "w") as file:
                    file.writelines(students)  # Overwrite the file with the updated list of students
                print(f"Student {target_student_id} was successfully deleted!")
                print("")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_students():
    students_filepath = "../files/students.txt"  # Relative filepath of the collection of students
    pages = {1: []}  # Initialize a dictionary that stores students

    try:
        with open(students_filepath, "r") as file:
            students = file.readlines()

            for student in students:
                student = student.strip('\n')
                if is_page_full(pages):
                    create_new_page(pages)
                write_to_page(pages, student)  # Stores the student in the latest available page

            print(f"There are {len(students)} students registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(f"Page {page} (First Entry: {pages.get(page)[0][0:5]})")  # Shows the first student ID of each page
                try:
                    print("")
                    target_page = int(input("Enter the desired page number (Enter 0 to exit): "))
                    if target_page == 0:  # Exit option for users
                        print("")
                        view_all_data()
                except ValueError:
                    pass
                if target_page > len(pages):  # Checks if the page exists
                    print(f"Page {target_page} does not exist!")
                else:
                    current_students = pages.get(target_page)
                    for student in current_students:
                        student_id, student_name, student_course, student_phone_number, student_email, student_gender, student_dob = student.split(',')
                        print(f"Student ID: {student_id}")
                        print(f"Student Name: {student_name}")
                        print(f"Student Course Code: {student_course}")
                        print(f"Student Phone Number: {student_phone_number}")
                        print(f"Student Email: {student_email}")
                        print(f"Student Gender: {student_gender}")
                        print(f"Student Date of Birth: {student_dob}")
                        print("=====================================")


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def change_student_name(student_id, students, current_name):  # Gets and edits the student name of the target student
    students_filepath = "../files/students.txt"

    print("")
    print(f"{student_id} name is currently {current_name}.")  # Shows current student name
    new_name = input(f"Enter {student_id}'s new name: ")  # Gets new student name

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(',')
            updated_student_info = f"{current_student_id},{new_name},{current_course_code},{current_phone_number},{current_email},{current_gender},{current_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)  # Overwrite the student save file
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def change_student_course(student_id, students, current_course):
    students_filepath = "../files/students.txt"
    courses_filepath = "../files/courses.txt"

    try:
        with open(courses_filepath, "r") as file:  # Opens file in read mode
            courses = file.readlines()
            available_course_codes = []
            for course in courses:  # Gets all the existing course codes that can be deleted
                available_course_codes.append(course[0:5])
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    print("")
    print(f"{student_id} course code is currently {current_course}.")

    new_course_code = ""
    while True:
        try:
            if len(new_course_code) != 5 or new_course_code not in available_course_codes:  # Length and uniqueness check for course code
                if len(available_course_codes) == 0:  # If there are no existing courses, no additional info is shown
                    pass
                else:  # Shows the last used course code
                    print(f"Last Used Course Code: {available_course_codes[len(available_course_codes) - 1]}")
                new_course_code = input("New Course Code (5 characters and unique): ")
            else:
                break
        except ValueError:
            pass

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(
                ',')
            updated_student_info = f"{current_student_id},{current_name},{new_course_code},{current_phone_number},{current_email},{current_gender},{current_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def change_student_phone_number(student_id, students, current_phone_number):
    students_filepath = "../files/students.txt"

    print("")
    print(f"{student_id} course code is currently {current_phone_number}.")
    new_phone_number = input(f"Enter {student_id}'s new phone number: ")

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(
                ',')
            updated_student_info = f"{current_student_id},{current_name},{current_course_code},{new_phone_number},{current_email},{current_gender},{current_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def change_student_email(student_id, students, current_email):
    students_filepath = "../files/students.txt"

    print("")
    print(f"{student_id} email is currently {current_email}.")

    new_email = ""
    while True:
        try:
            if '@' and '.' not in new_email:  # Uniqueness check for course code
                new_email = input(f"Enter {student_id}'s new email: ")
            else:
                break
        except ValueError:
            pass

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(
                ',')
            updated_student_info = f"{current_student_id},{current_name},{current_course_code},{current_phone_number},{new_email},{current_gender},{current_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def change_student_gender(student_id, students, current_gender):
    students_filepath = "../files/students.txt"

    print("")
    print(f"{student_id} gender is currently {current_gender}.")

    new_gender = input(f"Enter {student_id}'s new gender (M/F): ")
    while True:
        try:
            if new_gender.lower() not in ['m', 'f']:  # Length and uniqueness check for course code
                new_gender = input(f"Enter {student_id}'s new gender (M/F): ")
            else:
                break
        except ValueError:
            pass

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(
                ',')
            updated_student_info = f"{current_student_id},{current_name},{current_course_code},{current_phone_number},{current_email},{new_gender},{current_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def change_student_dob(student_id, students, current_dob):
    students_filepath = "../files/students.txt"

    print("")
    print(f"{student_id} gender is currently {current_dob}.")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            new_year = int(input(f"Enter {student_id}'s new birth year : "))  # Gets the user's input
            if new_year in range(1970, 2011):  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a year between 1970 and 2010!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a year between 1970 and 2010!")
            print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            new_month = int(input(f"Enter {student_id}'s new birth month (1-12) : "))  # Gets the user's input
            if new_month in range(1, 13):  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 12!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 12!")
            print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            if new_month in [1, 3, 5, 7, 8, 10, 12]:
                new_day = int(input(f"Enter {student_id}'s new birth day (1-31) : "))  # Gets the user's input
                if new_day in range(1, 32):  # Checks if the user input is valid
                    break  # Stops the while loop
                else:
                    print("You need to enter a value between 1 and 31!")
                    print("")
            elif new_month in [4, 6, 9, 11]:
                new_day = int(input(f"Enter {student_id}'s new birth day (1-30) : "))  # Gets the user's input
                if new_day in range(1, 31):  # Checks if the user input is valid
                    break  # Stops the while loop
                else:
                    print("You need to enter a value between 1 and 30!")
                    print("")
            elif new_month == 2 and new_year % 4 == 0:
                new_day = int(input(f"Enter {student_id}'s new birth day (1-29) : "))  # Gets the user's input
                if new_day in range(1, 30):  # Checks if the user input is valid
                    break  # Stops the while loop
                else:
                    print("You need to enter a value between 1 and 29!")
                    print("")
            elif new_month == 2 and new_year % 4 != 0:
                new_day = int(input(f"Enter {student_id}'s new birth day (1-28) : "))  # Gets the user's input
                if new_day in range(1, 29):  # Checks if the user input is valid
                    break  # Stops the while loop
                else:
                    print("You need to enter a value between 1 and 28!")
                    print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter an integer value!")
            print("")

    new_dob = f"{new_day}-{new_month}-{new_year}"

    for student in students:
        if student[0:5] == student_id:
            index = students.index(student)
            target_student = student
            current_student_id, current_name, current_course_code, current_phone_number, current_email, current_gender, current_dob = target_student.split(
                ',')
            updated_student_info = f"{current_student_id},{current_name},{current_course_code},{current_phone_number},{current_email},{current_gender},{new_dob}"
            students[index] = updated_student_info

            try:
                with open(students_filepath, 'w') as file:
                    file.writelines(students)
                print("")
                print("Student Info Updated Successfully")
                manage_students_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")


def manage_lecturers_menu():
    print("======================")
    print("Lecturer Management Menu")
    print("======================")
    print("1) Add A Lecturer")
    print("2) Remove A Lecturer")
    print("3) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3): "))  # Gets the user's input
            if choice in [1, 2, 3]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 3!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 3!")
            print("")

    match choice:
        case 1:
            add_lecturer()
        case 2:
            delete_lecturer()
        case 3:
            admin_menu()


def add_lecturer():
    lecturers_filepath = "../files/lecturers.txt"
    modules_filepath = "../files/modules.txt"
    faculty_filepath = "../files/faculty.txt"

    try:
        with open(faculty_filepath, "r") as file:
            faculties = file.readlines()
            available_faculty_code = []
            for faculty in faculties:
                available_faculty_code.append(faculty[0:2])
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(modules_filepath, "r") as file2:
            modules = file2.readlines()
            existing_module_codes = []
            for module in modules:
                existing_module_codes.append(module[0:5])
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    if len(available_faculty_code) == 0:
        print("You need to create a faculty first before registering a lecturer!")
        admin_menu()

    if len(existing_module_codes) == 0:
        print("You need to create a module first before registering a lecturer!")
        admin_menu()

    print("============")
    print("Add A Lecturer")
    print("============")
    print("")

    try:
        with open(lecturers_filepath, "r") as file:
            lecturers = file.readlines()
            used_lecturer_ids = []
            for lecturer in lecturers:
                used_lecturer_ids.append(lecturer[0:4])

            lecturer_id = ""
            while True:
                try:
                    if len(lecturer_id) != 4 or lecturer_id in used_lecturer_ids:
                        if len(used_lecturer_ids) == 0:
                            pass
                        else:
                            print(f"Last Used Lecturer ID: {used_lecturer_ids[len(used_lecturer_ids) - 1]}")
                        lecturer_id = input("Lecturer ID (4 characters and unique): ")
                    else:
                        break
                except ValueError:
                    pass

            lecturer_name = input("Lecturer Name: ")

            lecturer_faculty_code = ""
            while True:
                try:
                    if len(lecturer_faculty_code) != 2 or lecturer_faculty_code not in available_faculty_code:
                        lecturer_faculty_code = input("Lecturer Faculty Code (2 characters and exists): ")
                    else:
                        break
                except ValueError:
                    pass

            while True:  # Repeats infinitely unless a valid choice is given
                try:
                    number_of_modules = int(input("Enter number of modules this lecturer is in-charge of (1/2/3/4): "))  # Gets the user's input
                    if number_of_modules in range(1, 5):  # Checks if the user input is valid
                        break  # Stops the while loop
                    else:
                        print("You need to enter a value between 1 and 4!")
                        print("")
                except ValueError:  # Exception handling in case a non-integer value is inputted
                    print("You need to enter a value between 1 and 4!")
                    print("")

            lecturer_modules = ["null"] * 4
            for i in range(number_of_modules):
                module_code = ""
                while True:
                    try:
                        if len(module_code) != 5 or module_code not in existing_module_codes:
                            print(f"Available Module Codes: {existing_module_codes}")
                            module_code = input("Module Code (5 characters and exists): ")
                            lecturer_modules[i] = module_code
                        else:
                            break
                    except ValueError:
                        pass
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    module_1 = lecturer_modules[0]
    module_2 = lecturer_modules[1]
    module_3 = lecturer_modules[2]
    module_4 = lecturer_modules[3]

    try:
        with open(lecturers_filepath, "a") as file:
            if used_lecturer_ids:
                entry = f"\n{lecturer_id},{lecturer_name},{lecturer_faculty_code},{module_1},{module_2},{module_3},{module_4}"
            else:
                entry = f"{lecturer_id},{lecturer_name},{lecturer_faculty_code},{module_1},{module_2},{module_3},{module_4}"

            file.write(entry)

            print("")
            print("Lecturer has been registered successfully!")
            print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    manage_lecturers_menu()


def delete_lecturer():
    lecturer_filepath = "../files/lecturers.txt"  # Relative filepath of collection of lecturer data
    try:
        with open(lecturer_filepath, "r") as file:  # Reads and fetches lecturer data
            lecturers = file.readlines()
            available_lecturer_ids = []
            for lecturer in lecturers:
                available_lecturer_ids.append(lecturer[0:4])
            if len(available_lecturer_ids) == 0:
                print("")
                print(
                    "There are no lecturers registered yet! Create one before you delete one.")
                print("")
                manage_lecturers_menu()

        target_lecturer_id = ""
        while True:
            try:
                if len(target_lecturer_id) != 4 or target_lecturer_id not in available_lecturer_ids:
                    if target_lecturer_id == 'exit':
                        manage_lecturers_menu()
                    else:
                        print(f"The latest lecturer ID in use is {available_lecturer_ids[len(available_lecturer_ids) - 1]}")
                        print("Enter 'exit' to return to previous menu.")
                        target_lecturer_id = input("Lecturer ID (4 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        if len(lecturers) == 1:
            open(lecturer_filepath, 'w').close()
            print(f"Lecturer {target_lecturer_id} was successfully deleted!")
            print("")
            manage_lecturers_menu()
        else:
            for lecturer in lecturers:
                if target_lecturer_id == lecturer[0:4]:
                    lecturers.pop(lecturers.index(lecturer))
            try:
                with open(lecturer_filepath, "w") as file:
                    file.writelines(lecturers)
                print(f"Lecturer {target_lecturer_id} was successfully deleted!")
                print("")
                manage_lecturers_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_lecturers():
    lecturers_filepath = "../files/lecturers.txt"
    pages = {1: []}

    try:
        with open(lecturers_filepath, "r") as file:
            lecturers = file.readlines()

            for lecturer in lecturers:
                lecturer = lecturer.strip('\n')
                if is_page_full(pages):
                    create_new_page(pages)
                write_to_page(pages, lecturer)

            print(f"There are {len(lecturers)} lecturers registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(f"Page {page} (First Entry: {pages.get(page)[0][0:4]})")
                try:
                    print("")
                    target_page = int(input("Enter the desired page number (Enter 0 to exit): "))
                    if target_page == 0:
                        print("")
                        view_all_data()
                except ValueError:
                    pass
                if target_page > len(pages):
                    print(f"Page {target_page} does not exist!")
                else:
                    current_lecturers = pages.get(target_page)
                    for lecturer in current_lecturers:
                        lecturer_id, lecturer_name, lecturer_faculty_code, module_1, module_2, module_3, module_4 = lecturer.split(
                            ',')
                        print(f"Lecturer ID: {lecturer_id}")
                        print(f"Lecturer Name: {lecturer_name}")
                        print(f"Lecturer Faculty Code: {lecturer_faculty_code}")
                        print(f"Assigned Module 1: {module_1}")
                        print(f"Assigned Module 2: {module_2}")
                        print(f"Assigned Module 3: {module_3}")
                        print(f"Assigned Module 4: {module_4}")
                        print("=====================================")


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def manage_faculties_menu():
    print("======================")
    print("Faculty Management Menu")
    print("======================")
    print("1) Add A Faculty")
    print("2) Remove A Faculty")
    print("3) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3): "))  # Gets the user's input
            if choice in [1, 2, 3]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 3!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 3!")
            print("")

    match choice:
        case 1:
            add_faculty()
        case 2:
            delete_faculty()
        case 3:
            admin_menu()


def add_faculty():
    faculties_filepath = "../files/faculty.txt"  # Relative filepath for the collection courses
    print("=============")
    print("Add A Faculty")
    print("=============")
    print("")

    try:
        with open(faculties_filepath, "r") as file:  # Reads the courses.txt file
            faculties = file.readlines()  # Gets all the current courses
            used_faculty_codes = []
            for faculty in faculties:
                used_faculty_codes.append(faculty[0:2])  # Gets all the course codes that have been used

            faculty_code = ""
            while True:
                try:
                    if len(faculty_code) != 2 or faculty_code in used_faculty_codes:  # Length and uniqueness check for course code
                        faculty_code = input("Faculty Code (2 characters and unique): ")
                    else:
                        break
                except ValueError:
                    pass

            faculty_name = input("Faculty Name: ")

    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(faculties_filepath, "a") as file:
            if used_faculty_codes:
                entry = f"{faculty_code},{faculty_name}\n"  # Compiles the info above into the format: course_code,course_name, course_credits
            else:
                entry = f"{faculty_code},{faculty_name}"

            file.write(entry)  # Writes the info to file

            print("")
            print("Faculty has been created successfully!")
            print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    manage_faculties_menu()  # Brings the user back to the faculties menu


def delete_faculty():
    faculties_filepath = "../files/faculty.txt"  # Relative filepath of collection of student data
    try:
        with open(faculties_filepath, "r") as file:  # Reads and fetches student data
            faculties = file.readlines()
            available_faculty_code = []
            for faculty in faculties:
                available_faculty_code.append(faculty[0:2])

        target_faculty_code = ""
        while True:
            try:
                if len(target_faculty_code) != 2 or target_faculty_code not in available_faculty_code:
                    if target_faculty_code == 'exit':
                        manage_faculties_menu()
                    if len(available_faculty_code) == 0:
                        print("")
                        print(
                            "There are no faculties registered yet! A faculty needs to be created before you can delete one!")
                        print("")
                        manage_faculties_menu()
                    else:
                        print("")
                        print("Available Faculty Codes:")
                        for faculty in available_faculty_code:
                            print(f"- {faculty}")
                        print("")
                        print("Enter 'exit' to return to previous menu.")
                        target_faculty_code = input("Faculty Code (2 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        if len(faculties) == 1:
            open(faculties_filepath, 'w').close()
            print(f"Faculty {target_faculty_code} was successfully deleted!")
            print("")
            manage_faculties_menu()
        else:
            for faculty in faculties:
                if target_faculty_code == faculty[0:2]:
                    faculties.pop(faculties.index(faculty))
            try:
                with open(faculties_filepath, "w") as file:
                    file.writelines(faculties)
                print(f"Faculty {target_faculty_code} was successfully deleted!")
                print("")
                manage_faculties_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_faculties():
    faculties_filepath = "../files/faculty.txt"
    pages = {1: []}

    try:
        with open(faculties_filepath, "r") as file:
            faculties = file.readlines()

            for faculty in faculties:
                faculty = faculty.strip('\n')
                if is_page_full(pages):
                    create_new_page(pages)
                write_to_page(pages, faculty)

            print(f"There are {len(faculties)} faculties registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(f"Page {page} (First Entry: {pages.get(page)[0][0:2]})")
                try:
                    print("")
                    target_page = int(input("Enter the desired page number (Enter 0 to exit): "))
                    if target_page == 0:
                        print("")
                        view_all_data()
                except ValueError:
                    pass
                if target_page > len(pages):
                    print(f"Page {target_page} does not exist!")
                else:
                    current_faculties = pages.get(target_page)
                    for faculty in current_faculties:
                        faculty_code, faculty_name = faculty.split(',')
                        print(f"Faculty Code: {faculty_code}")
                        print(f"Faculty Name: {faculty_name}")
                        print("=====================================")


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def manage_modules_menu():
    print("======================")
    print("Module Management Menu")
    print("======================")
    print("1) Add A Module")
    print("2) Remove A Module")
    print("3) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3): "))  # Gets the user's input
            if choice in [1, 2, 3]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 3!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 3!")
            print("")

    match choice:
        case 1:
            add_modules()
        case 2:
            delete_modules()
        case 3:
            admin_menu()


def add_modules():
    modules_filepath = "../files/modules.txt"  # Relative filepath for the collection courses
    print("============")
    print("Add A Module")
    print("============")
    print("")

    try:
        with open(modules_filepath, "r") as file:  # Reads the courses.txt file
            modules = file.readlines()  # Gets all the current courses
            used_module_codes = []
            for module in modules:
                used_module_codes.append(module[0:5])  # Gets all the course codes that have been used

            module_code = ""
            while True:
                try:
                    if len(module_code) != 5 or module_code in used_module_codes:  # Length and uniqueness check for course code
                        module_code = input("Module Code (5 characters and unique): ")
                    else:
                        break
                except ValueError:
                    pass

            module_name = input("Module Name: ")

    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(modules_filepath, "a") as file:
            if used_module_codes:
                entry = f"{module_code},{module_name}\n"  # Compiles the info above into the format: course_code,course_name, course_credits
            else:
                entry = f"{module_code},{module_name}"

            file.write(entry)  # Writes the info to file

            print("")
            print("Module has been created successfully!")
            print("")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    manage_modules_menu()  # Brings the user back to the faculties menu


def delete_modules():
    modules_filepath = "../files/modules.txt"  # Relative filepath of collection of student data
    try:
        with open(modules_filepath, "r") as file:  # Reads and fetches student data
            modules = file.readlines()
            available_module_code = []
            for module in modules:
                available_module_code.append(module[0:5])

        target_module_code = ""
        while True:
            try:
                if len(target_module_code) != 5 or target_module_code not in available_module_code:
                    if target_module_code == 'exit':
                        manage_modules_menu()
                    if len(available_module_code) == 0:
                        print("")
                        print(
                            "There are no modules registered yet! A module needs to be created before you can delete one!")
                        print("")
                        manage_faculties_menu()
                    else:
                        print("")
                        print("Available Module Codes:")
                        for module in available_module_code:
                            print(f"- {module}")
                        print("")
                        print("Enter 'exit' to return to previous menu.")
                        target_module_code = input("Module Code (2 characters and exists): ")
                else:
                    break
            except ValueError:
                pass

        if len(modules) == 1:
            open(modules_filepath, 'w').close()
            print(f"Module {target_module_code} was successfully deleted!")
            print("")
            manage_faculties_menu()
        else:
            for module in modules:
                if target_module_code == module[0:5]:
                    modules.pop(modules.index(module))
            try:
                with open(modules_filepath, "w") as file:
                    file.writelines(modules)
                print(f"Module {target_module_code} was successfully deleted!")
                print("")
                manage_modules_menu()
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def view_modules():
    modules_filepath = "../files/modules.txt"
    pages = {1: []}

    try:
        with open(modules_filepath, "r") as file:
            modules = file.readlines()

            for module in modules:
                module = module.strip('\n')
                if is_page_full(pages):
                    create_new_page(pages)
                write_to_page(pages, module)

            print(f"There are {len(modules)} modules registered stored in {len(pages)} page(s).")
            print("")

            while True:
                for page in pages:
                    print(f"Page {page} (First Entry: {pages.get(page)[0][0:5]})")
                try:
                    print("")
                    target_page = int(input("Enter the desired page number (Enter 0 to exit): "))
                    if target_page == 0:
                        print("")
                        view_all_data()
                except ValueError:
                    pass
                if target_page > len(pages):
                    print(f"Page {target_page} does not exist!")
                else:
                    current_modules = pages.get(target_page)
                    for module in current_modules:
                        module_code, module_name = module.split(',')
                        print(f"Module Code: {module_code}")
                        print(f"Module Name: {module_name}")
                        print("=====================================")


    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def generate_report():
    students_filepath = "../files/students.txt"
    courses_filepath = "../files/courses.txt"
    faculties_filepath = "../files/faculty.txt"
    modules_filepath = "../files/modules.txt"
    lecturers_filepath = "../files/lecturers.txt"

    try:
        with open(students_filepath, "r") as file:
            students = file.readlines()
            total_students = len(students)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(courses_filepath, "r") as file:
            courses = file.readlines()
            total_courses = len(courses)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(faculties_filepath, "r") as file:
            faculties = file.readlines()
            total_faculties = len(faculties)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(modules_filepath, "r") as file:
            modules = file.readlines()
            total_modules = len(modules)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(lecturers_filepath, "r") as file:
            lecturers = file.readlines()
            total_lecturers = len(lecturers)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    print("======================")
    print("Generated Admin Report")
    print("======================")
    print("")
    print(f"| Total Registered Students: {total_students}")
    print(f"| Total Registered Courses: {total_courses}")
    print(f"| Total Registered Modules: {total_modules}")
    print(f"| Total Registered Faculties: {total_faculties}")
    print(f"| Total Registered Lecturers: {total_lecturers}")
    print("")

    admin_menu()


def view_all_data():
    students_filepath = "../files/students.txt"
    courses_filepath = "../files/students.txt"
    faculties_filepath = "../files/faculty.txt"
    modules_filepath = "../files/modules.txt"
    lecturers_filepath = "../files/lecturers.txt"

    try:
        with open(students_filepath, "r") as file:
            students = file.readlines()
            total_students = len(students)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(lecturers_filepath, "r") as file:
            lecturers = file.readlines()
            total_lecturers = len(lecturers)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(courses_filepath, "r") as file:
            courses = file.readlines()
            total_courses = len(courses)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(faculties_filepath, "r") as file:
            faculties = file.readlines()
            total_faculties = len(faculties)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        with open(modules_filepath, "r") as file:
            modules = file.readlines()
            total_modules = len(modules)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    print("=============")
    print("View All Data")
    print("=============")
    print("")
    print(f"| Total Registered Courses: {total_courses}")
    print(f"| Total Registered Students: {total_students}")
    print(f"| Total Registered Lecturers: {total_lecturers}")
    print(f"| Total Registered Modules: {total_modules}")
    print(f"| Total Registered Faculties: {total_faculties}")
    print("")
    print("1) View All Registered Courses")
    print("2) View All Registered Data")
    print("3) View All Registered Lecturers")
    print("4) View All Registered Modules")
    print("5) View All Registered Faculties")
    print("6) Back to Admin Menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))  # Gets the user's input
            if choice in [1, 2, 3, 4, 5, 6]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 6!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 6!")
            print("")

    match choice:
        case 1:
            view_courses()
        case 2:
            view_students()
        case 3:
            view_lecturers()
        case 4:
            view_modules()
        case 5:
            view_faculties()
        case 6:
            admin_menu()


def admin_logout():
    print("")
    print("You've been logged out! Sending you to the main menu...")
    print("")

    main_menu()


def register_admin():
    admin_filepath = "../files/admins.txt"  # Relative filepath for the text file where account details are stored
    registered_usernames = []  # Pre-initialized array for usernames in the file

    try:
        with open(admin_filepath, "r") as file:  # Gets all the usernames in the file and appends to the array
            admin_accounts = file.readlines()
            for account in admin_accounts:
                username, password = account.split(",")
                registered_usernames.append(username)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        file = open(admin_filepath, "a")

        print("")
        print("==============")
        print("Create Account")
        print("==============")

        admin_id = ""  # Gets new user ID
        while True:
            try:
                if len(admin_id) < 4 or admin_id in registered_usernames:  # Length and uniqueness check for the ID
                    admin_id = input("Username (min. 4 characters and unique): ")
                else:
                    break
            except ValueError:
                pass

        admin_password = ""  # Gets user password
        while True:
            try:
                if len(admin_password) < 7:  # Length check for the password
                    admin_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        file.write(f"\n{admin_id},{admin_password}")  # Writes the new account to file

        print("")
        print("Administrator account created successfully!")

        file.close()  # Close the file
        account_registration_menu()  # Brings user back to registration menu
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def register_lecturer():
    lecturer_filepath = "../files/lecturer_accounts.txt"  # Relative filepath for the text file where account details are stored
    registered_usernames = []  # Pre-initialized array for usernames in the file

    try:
        with open(lecturer_filepath, "r") as file:  # Gets all the usernames in the file and appends to the array
            lecturer_accounts = file.readlines()
            for account in lecturer_accounts:
                username, password = account.split(",")
                registered_usernames.append(username)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        file = open(lecturer_filepath, "a")

        print("")
        print("==============")
        print("Create Account")
        print("==============")

        lecturer_id = ""  # Gets new user ID
        while True:
            try:
                if len(lecturer_id) < 4 or lecturer_id in registered_usernames:  # Length and uniqueness check for the ID
                    lecturer_id = input("Username (min. 4 characters and unique): ")
                else:
                    break
            except ValueError:
                pass

        lecturer_password = ""  # Gets user password
        while True:
            try:
                if len(lecturer_password) < 7:  # Length check for the password
                    lecturer_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        if registered_usernames:
            file.write(f"\n{lecturer_id},{lecturer_password}")  # Writes the new account to file
        else:
            file.write(f"{lecturer_id},{lecturer_password}")


        print("")
        print("Lecturer account created successfully!")

        file.close()  # Close the file
        account_registration_menu()  # Brings user back to registration menu
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def register_student():
    students_filepath = "../files/student_accounts.txt"  # Relative filepath for the text file where account details are stored
    registered_usernames = []  # Pre-initialized array for usernames in the file

    try:
        with open(students_filepath, "r") as file:  # Gets all the usernames in the file and appends to the array
            student_accounts = file.readlines()
            for account in student_accounts:
                username, password = account.split(",")
                registered_usernames.append(username)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        file = open(students_filepath, "a")

        print("")
        print("==============")
        print("Create Account")
        print("==============")

        student_id = ""  # Gets new user ID
        while True:
            try:
                if len(student_id) < 4 or student_id in registered_usernames:  # Length and uniqueness check for the ID
                    student_id = input("Username (min. 4 characters and unique): ")
                else:
                    break
            except ValueError:
                pass

        student_password = ""  # Gets user password
        while True:
            try:
                if len(student_password) < 7:  # Length check for the password
                    student_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        if registered_usernames:
            file.write(f"\n{student_id},{student_password}")  # Writes the new account to file
        else:
            file.write(f"{student_id},{student_password}")

        print("")
        print("Student account created successfully!")

        file.close()  # Close the file
        account_registration_menu()  # Brings user back to registration menu
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def register_registrar():
    registrar_filepath = "../files/registrars.txt"  # Relative filepath for the text file where account details are stored
    registered_usernames = []  # Pre-initialized array for usernames in the file

    try:
        with open(registrar_filepath, "r") as file:  # Gets all the usernames in the file and appends to the array
            registrar_accounts = file.readlines()
            for account in registrar_accounts:
                username, password = account.split(",")
                registered_usernames.append(username)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        file = open(registrar_filepath, "a")

        print("")
        print("==============")
        print("Create Account")
        print("==============")

        registrar_id = ""  # Gets new user ID
        while True:
            try:
                if len(registrar_id) < 4 or registrar_id in registered_usernames:  # Length and uniqueness check for the ID
                    registrar_id = input("Username (min. 4 characters and unique): ")
                else:
                    break
            except ValueError:
                pass

        registrar_password = ""  # Gets user password
        while True:
            try:
                if len(registrar_password) < 7:  # Length check for the password
                    registrar_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        if registered_usernames:
            file.write(f"\n{registrar_id},{registrar_password}")  # Writes the new account to file
        else:
            file.write(f"{registrar_id},{registrar_password}")

        print("")
        print("Registrar account created successfully!")

        file.close()  # Close the file
        account_registration_menu()  # Brings user back to registration menu
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def register_accountant():
    accountants_filepath = "../files/accountants.txt"  # Relative filepath for the text file where account details are stored
    registered_usernames = []  # Pre-initialized array for usernames in the file

    try:
        with open(accountants_filepath, "r") as file:  # Gets all the usernames in the file and appends to the array
            accountant_accounts = file.readlines()
            for account in accountant_accounts:
                username, password = account.split(",")
                registered_usernames.append(username)
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    try:
        file = open(accountants_filepath, "a")

        print("")
        print("==============")
        print("Create Account")
        print("==============")

        accountant_id = ""  # Gets new user ID
        while True:
            try:
                if len(accountant_id) < 4 or accountant_id in registered_usernames:  # Length and uniqueness check for the ID
                    accountant_id = input("Username (min. 4 characters and unique): ")
                else:
                    break
            except ValueError:
                pass

        accountant_password = ""  # Gets user password
        while True:
            try:
                if len(accountant_password) < 7:  # Length check for the password
                    accountant_password = input("Password (min. 7 characters): ")
                else:
                    break
            except ValueError:
                pass

        if registered_usernames:
            file.write(f"\n{accountant_id},{accountant_password}")  # Writes the new account to file
        else:
            file.write(f"{accountant_id},{accountant_password}")

        print("")
        print("Accountant account created successfully!")

        file.close()  # Close the file
        account_registration_menu()  # Brings user back to registration menu
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")


def account_registration_menu():
    print("=========================")
    print("Account Registration Menu")
    print("=========================")
    print("What account do you wish to register?")
    print("")
    print("1) Administrator")
    print("2) Lecturer")
    print("3) Student")
    print("4) Registrar")
    print("5) Accountant")
    print("6) Return to previous menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))  # Gets the user's input
            if choice in [1, 2, 3, 4, 5, 6]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 6!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 6!")
            print("")

    match choice:
        case 1:
            register_admin()
        case 2:
            register_lecturer()
        case 3:
            register_student()
        case 4:
            register_registrar()
        case 5:
            register_accountant()
        case 6:
            admin_menu()


def main_menu():
    check_students_file()
    check_faculties_file()
    check_fees_files()
    check_courses_file()
    check_grades_file()
    check_modules_file()
    check_lecturers_file()
    check_registrar_file()
    check_accountant_file()
    check_admin_file()
    check_backup_date_file()
    check_student_account_file()
    check_lecturer_account_file()
    check_backup_date()

    print("============================================")  # Prints the selection menu for the UMS
    print("Welcome to the University Management System!")
    print("============================================")
    print("")
    print("Are you a(n): ")
    print("")
    print("1) Administrator")
    print("2) Lecturer")
    print("3) Student")
    print("4) Registrar")
    print("5) Accountant")
    print("")
    print("Enter 6 if you wish two exit the program.")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2/3/4/5/6): "))  # Gets the user's input
            if choice in [1, 2, 3, 4, 5, 6]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 6!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 6!")
            print("")

    match choice:
        case 1:
            login_admin()  # Login page for administrators
        case 2:
            login_lecturer()  # Login page for lecturers
        case 3:
            login_student()  # Login page for students
        case 4:
            login_registrar()  # Login page for Registrar
        case 5:
            login_accountant()  # Login page for accountants
        case 6:
            exit()  # Exits the program

# END OF ADMINISTRATOR AND MAIN MENU MODULE
# START OF ACCOUNTANT MODULE


# File name for storing fees data
FEES_FILE = "../files/fees.txt"
COURSES_FILE = "../files/courses.txt"
STUDENTS_FILE = "../files/students.txt"


def login_accountant():  # The login page for accountant
    print("")
    print("========================")
    print("Accountant Login Page")
    print("========================")

    accountant_id = ""
    while True:
        if len(accountant_id) < 4:  # Length check for the accountant username
            accountant_id = input("Username (min. 4 characters): ")
        else:
            break

    accountant_password = ""
    while True:
        if len(accountant_password) < 7:  # Length check for the accountant password
            accountant_password = input("Password (min. 7 characters): ")
        else:
            break

    check_accountant_login(accountant_id, accountant_password)  # Sends the username and password to check_admin_login()


def check_accountant_login(user_id, user_password):  # Checks if the username and password provided exists and matches
    accountants_filepath = "../files/accountants.txt"  # Relative filepath for the collection of accountant usernames and passwords
    success = False
    try:
        with open(accountants_filepath, "r") as file:
            accounts = file.readlines()  # Fetches all accountant accounts stored
    except FileNotFoundError:
        print("An error has occurred! The file was not found. Please contact developer.")

    for account in accounts:  # Parses the comma separated values into individual values
        username, password = account.split(',')  # Account is always stored in the format: username,password
        if user_id == username.strip('\n'):  # Checks if username exists
            if user_password == password.strip('\n'):  # If username exists, checks if passwords match
                login_accountant_success()
            else:
                login_accountant_fail()
    if not success:
        login_accountant_fail()


def login_accountant_success():  # Shows success message and sends user to the main accountant menu
    print("")
    print("Accountant login successful!")
    print("")

    accountant_menu()


def login_accountant_fail():  # Gives the user options to try again or to choose their account type again.
    print("")
    print("The username/password you enter is incorrect! Would you like to:")
    print("1) Try again")
    print("2) Return to main menu")
    print("")

    while True:  # Repeats infinitely unless a valid choice is given
        try:
            choice = int(input("Enter your choice (1/2): "))  # Gets the user's input
            if choice in [1, 2]:  # Checks if the user input is valid
                break  # Stops the while loop
            else:
                print("You need to enter a value between 1 and 2!")
                print("")
        except ValueError:  # Exception handling in case a non-integer value is inputted
            print("You need to enter a value between 1 and 2!")
            print("")

    match choice:
        case 1:
            login_accountant()
        case 2:
            main_menu()


def record_tuition_fee():  # Function to record tuition fees
    try:
        print("")
        print("===================")
        print("Record Tuition Fees")
        print("===================")
        print("")

        student_id = input("Enter Student ID (5 characters long and exists): ")

        with open(FEES_FILE, "r") as fees_file:  # Check if the student already has a record
            for line in fees_file:
                file_student_id, file_student_name, file_course_code, file_amount_paid, file_amount_due = line.strip().split(",")
                if file_student_id == student_id:
                    print("Sorry, this student already has a record.")
                    print("Please use the 'Update Payment Records' option to update the payment.")
                    return

        # Search for student details in students.txt
        with open(STUDENTS_FILE, "r") as student_file:  # Search for the student details in the students.txt file
            for line in student_file:
                file_student_id, file_student_name, file_student_course_code, file_student_phone_number, file_student_email, file_student_gender, file_student_dob = line.strip().split(",")
                if file_student_id == student_id:
                    break

            else:  # If student not found, display error and exit
                print("Sorry, student ID not found in the records.")
                print("Please enter a valid Student ID!")
                return

        # Display student details
        print("")
        print(f"Student Found")
        print("")
        print(f"Student ID: {file_student_id}")
        print(f"Student Name: {file_student_name}")
        print(f"Student Course Code: {file_student_course_code}")
        print(f"Student Phone Number: {file_student_phone_number}")
        print(f"Student Gmail: {file_student_email}")
        print(f"Student Gender (M/F): {file_student_gender}")
        print(f"Student D.O.B.: {file_student_dob}\n")

        course_code = file_student_course_code  # Fetch the course fee based on the course code
        course_fee = None
        with open(COURSES_FILE, "r") as courses_file:
            for line in courses_file:
                file_course_code, file_course_name, file_course_credits, file_course_fee = line.strip().split(",")
                if file_course_code == course_code:
                    course_fee = float(file_course_fee)
                    break

        # If the course code is not found
        if course_fee is None:
            print(f"Error: Course code {file_course_code} not found in the records.")
            return

        print(f"Course Fee for {file_course_code}: ${course_fee:.2f}")

        confirmation = input("Do you want to proceed with payment? (Yes/No): ").strip().lower()
        if confirmation != "yes":
            print("Returning to menu...")
            return

        # Prompt for tuition fee details
        amount_paid = float(input("Enter Amount Paid: "))

        # Validate amounts
        if amount_paid < 0:
            print("Sorry, amounts cannot be negative.")
            print("Please try again.")
            return

        if course_fee < amount_paid:
            print("Payment exceeds the course fee.")
            print("Please try again. ")
            return

        amount_due = course_fee - amount_paid  # Calculate the outstanding fee

        # Write fee details to student_fees.txt
        with open(FEES_FILE, "a") as fees_file:
            fees_file.write(f"{student_id},{file_student_name},{course_code},{amount_paid},{amount_due}\n")

        print("Tuition fee recorded successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}. Ensure the students.txt file exists.")
    except ValueError:
        print("Please enter a valid student ID.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Function to view outstanding fees
def view_outstanding_fees():
    try:
        print("\n================")
        print("Outstanding Fees")
        print("================")

        with open(FEES_FILE, "r") as fees_file, open(COURSES_FILE, "r") as courses_file:
            # Build a course fee dictionary for quick lookup
            course_fees = {}
            for line in courses_file:
                course_code, course_name, course_credits, course_fee = line.strip().split(",")
                course_fees[course_code] = float(course_fee)

            print("\nStudents with Outstanding Fees:")
            print("{:<10} {:<15} {:>15}".format("ID", "Name", "Outstanding Amount"))
            print("-" * 45)

            found = False
            for line in fees_file:
                student_id, student_name, student_course_code, amount_paid, amount_due = line.strip().split(",")

                # Calculate outstanding fee
                amount_due = float(amount_due)


                if amount_due > 0:
                    print("{:<10} {:<20} ${:>10.2f}".format(student_id, student_name, amount_due))
                    found = True

            if not found:
                print("No students with outstanding fees.")
    except FileNotFoundError:
        print("No fee records found. Please record fees first.")
    except Exception as e:
        print(f"An error occurred while viewing outstanding fees: {e}")


# Function to update payment records
def update_payment_record():
    print("\n======================")
    print("Update Payment Records")
    print("======================")

    try:
        student_id = input("Enter Student ID to update payment: ")
        found = False
        updated_data = []

        with open(FEES_FILE, "r") as file:
            for line in file:
                file_student_id, file_student_name, file_student_course_code, file_amount_paid, file_amount_due = line.strip().split(",")

                if file_student_id == student_id:  # show student's details
                    print("\nCurrent Record: ")
                    print(f"Student name: {file_student_name}")
                    print(f"Student ID: {file_student_id}")
                    print(f"Student Course Code: {file_student_course_code}")
                    print(f"Amount Paid: ${float(file_amount_paid):.2f}")
                    print(f"Amount Due: ${float(file_amount_due):.2f}")

                    if float(file_amount_due) <= 0:  # No outstanding payment
                        print("\nNo amount due for this student")
                        print("No updates required.")
                        return

                    amount_paid = float(input("\nEnter Additional Payment Amount: "))
                    if amount_paid < 0:
                        print("Payment cannot be negative.")
                        print("Please try again.")
                        return

                    new_amount_paid = float(file_amount_paid) + amount_paid
                    new_amount_due = float(file_amount_due) - amount_paid

                    if new_amount_due < 0:
                        print("Error: Payment exceeds the due amount.")
                        print("Please try again.")
                        return

                    print(f"\nUpdated Record:")
                    print(f"Amount Paid: ${new_amount_paid:.2f}")
                    print(f"Amount Due: ${new_amount_due:.2f}")
                    updated_data.append(f"{file_student_id},{file_student_name},{file_student_course_code},{new_amount_paid},{new_amount_due}")
                    found = True
                else:
                    # Keep unchanged records
                    updated_data.append(f"{file_student_id},{file_student_name},{file_student_course_code},{file_amount_paid},{file_amount_due}")

        if not found:
            print("\nStudent ID not found.")
            print("Please update your tuition fee record before accessing this option.")
            return

        with open(FEES_FILE, "w") as file:
            for record in updated_data:
                file.write(record + "\n")

        print("Payment record updated successfully.")
    except FileNotFoundError:
        print("No fee records found. Please record fees first.")
    except ValueError:
        print("Invalid input. Please enter valid number for the payment amount.")
    except Exception as e:
        print(f"An error occurred while updating payment records: {e}")


# Function to issue a fee receipt
def issue_fee_receipt():
    print("\n==================")
    print("Issue Fee Receipts")
    print("==================")

    try:  # Enter student ID to generate receipts
        student_id = input("Enter Student ID to issue receipt: ")
        with open(FEES_FILE, "r") as file:
            for line in file:
                file_student_id, file_student_name, file_amount_paid, file_student_course_code, file_amount_due = line.strip().split(",")
                if file_student_id == student_id:
                    receipt_file = f"../receipts/receipt_{student_id}.txt"
                    with open(receipt_file, "w") as receipt:
                        receipt.write("University Management System\n")
                        receipt.write("-" * 40 + "\n")
                        receipt.write(f"Receipt for Student ID: {file_student_id}\n")
                        receipt.write(f"Name: {file_student_name}\n")
                        receipt.write(f"Course Code: {file_amount_paid}\n")
                        receipt.write(f"Amount Paid: ${file_student_course_code}\n")
                        receipt.write(f"Amount Due: ${file_amount_due}\n")
                        receipt.write("-" * 40 + "\n")
                        receipt.write("Thank you for your payment.\n")
                    print(f"Receipt issued successfully for {file_student_id} at {receipt_file}")
                    return
        print("\nStudent ID not found.")  # if student id not found in students_fee.txt
        print("Please update your tuition fee record before accessing this option.")
    except FileNotFoundError:
        print("No fee records found. Please record fees first.")
    except Exception as e:
        print(f"An error occurred while issuing receipt: {e}")


# Function to view financial summary
def view_financial_summary():

    print("\n=================")
    print("Financial Summary")
    print("=================")
    try:  # Store the amounts by all student (ttl paid and ttl due)
        total_paid = 0
        total_due = 0

        with open(FEES_FILE, "r") as file:  # Open students fee file and calculate totals
            for line in file:
                student_id, student_name, student_course_code, amount_paid, amount_due = line.strip().split(",")
                total_paid += float(amount_paid)
                total_due += float(amount_due)

        # Display the total
        print(f"Total Fees Collected: ${total_paid}")
        print(f"Total Outstanding Fees: ${total_due}")
    except FileNotFoundError:
        print("No fee records found. Please record fees first.")
    except Exception as e:
        print(f"An error occurred while viewing financial summary: {e}")


# Function to view summary by course
def view_course_summary():
    try:
        print("\n=========================")
        print("View Fee Summary by Course")
        print("=========================")

        # Course data will map each course code to its fees and names
        course_data = {}
        with open(COURSES_FILE, "r") as courses_file:
            for line in courses_file:
                course_code, course_name, course_credits, course_fee = line.strip().split(",")
                course_data[course_code] = {"name": course_name, "paid": 0.0, "due": 0.0}

        # Read fee data and calculate totals by course
        with open(FEES_FILE, "r") as fees_file:
            for line in fees_file:
                student_id, student_name, student_course_code, amount_paid, amount_due = line.strip().split(",")
                amount_paid = float(amount_paid)
                amount_due = float(amount_due)

                if student_course_code in course_data:  # check if the course code from the student fee file exist in course data
                    course_data[student_course_code]["paid"] += amount_paid
                    course_data[student_course_code]["due"] += amount_due

        # Display the course summary
        print("\n{:<10} {:<20} {:>15} {:>15}".format("Course", "Course Name", "Total Paid", "Total Due"))
        print("-" * 60)

        for course_code, data in course_data.items():
            print("{:<10} {:<20} ${:>14.2f} ${:>14.2f}".format(
                course_code, data["name"], data["paid"], data["due"]
            ))

    except FileNotFoundError:
        print("Course or fee records not found. Please ensure all files exist.")
    except Exception as e:
        print(f"An error occurred while viewing course summary: {e}")


# Main menu for accountant functionalities
def accountant_menu():
    while True:
        print("\n=================================")
        print("---WELCOME TO ACCOUNTANT MENU!---")
        print("=================================")
        print("1. Record Tuition Fees")
        print("2. View Outstanding Fees")
        print("3. Update Payment Records")
        print("4. Issue Fee Receipt")
        print("5. View Financial Summary")
        print("6. View Summary by Course")
        print("7. Log Out")
        print("")

        choice = input("Enter your choice: ")

        if choice == "1":
            record_tuition_fee()
        elif choice == "2":
            view_outstanding_fees()
        elif choice == "3":
            update_payment_record()
        elif choice == "4":
            issue_fee_receipt()
        elif choice == "5":
            view_financial_summary()
        elif choice == "6":
            view_course_summary()
        elif choice == "7":
            print("Exiting Accountant Menu.")
            main_menu()
        else:
            print("You need to enter a value between 1 and 7! Please try again.")


# END OF ACCOUNTANT MODULE

# START OF LECTURER MODULE

# File paths for lecturer data management
MODULES_FILE = "files/modules.txt"
GRADES_FILE = "files/grades.txt"
ATTENDANCE_FILE = "files/attendance.txt"
LECTURERS_FILE = "files/lecturers.txt"
LECTURER_ACCOUNT_FILE = "files/lecturer_accounts.txt"

# Helper functions for file operations


def file_exists_lecturer(file_path):
    try:
        with open(file_path, "r"):
            return True
    except FileNotFoundError:
        return False


def read_file(file_path):
    if not file_exists_lecturer(file_path):
        print(f"Error: File '{file_path}' not found. Please create it.")
        return []
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return []


def append_to_file_lecturer(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")


def validate_input_lecturer(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options and user_input not in valid_options:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")
        else:
            return user_input


def get_module_name(module_code):
    """
    Retrieves the module name for a given module code from modules.txt.
    """
    modules = read_file(MODULES_FILE)

    for module in modules:
        fields = module.strip().split(",", 1)
        if fields[0] == module_code:
            return fields[1]
    return None


# Lecturer functionalities
def view_assigned_modules(modules):
    valid_modules = [module for module in modules if module != "null"]
    if not valid_modules:
        print("No modules assigned to you.")
        return

    print("Your Assigned Modules:")
    for module_code in valid_modules:
        module_name = get_module_name(module_code)
        if module_name:
            print(f"- {module_code}: {module_name}")
        else:
            print(f"- {module_code}: [Module Name Not Found]")


def get_lecturer_data(lecturer_id):
    """
    Retrieves lecturer data for the given lecturer_id.
    """
    lecturers = read_file(LECTURERS_FILE)


    for lecturer in lecturers:

        try:
            fields = lecturer.strip().split(",")
            if fields[0] == lecturer_id:
                data = {
                    "id": fields[0],
                    "name": fields[1],
                    "program": fields[2],  # Program
                    "modules": fields[3:6],  # Modules
                }
                return data
        except IndexError:
            print(f"Skipping malformed entry: {lecturer}")
    return None


def get_lecturer_password(lecturer_id):
    """
    Retrieve the password for a given lecturer_id from lecturer-account.txt.
    Format: lecturer_id,password
    """
    accounts = read_file(LECTURER_ACCOUNT_FILE)
    for acc in accounts:
        fields = acc.strip().split(",")
        if len(fields) == 2 and fields[0] == lecturer_id:
            return fields[1]  # Return the password
    return None


def lecturer_login():
    """
    Handles lecturer login by verifying Lecturer ID and password against lecturer-account.txt.
    If invalid, prompts again or allows user to exit.
    """
    while True:
        lecturer_id = input("Enter your Lecturer ID (or type 'exit' to quit): ").strip()
        if lecturer_id.lower() == "exit":
            print("Exiting program.")
            return None  # Exit the login process gracefully

        # Retrieve password for the given Lecturer ID
        password = get_lecturer_password(lecturer_id)
        if not password:
            print("Invalid Lecturer ID. Please try again.")
            continue

        # Prompt for password
        password_attempt = input("Enter your password: ").strip()
        if password_attempt == password:
            # Successful login
            lecturer_data = get_lecturer_data(lecturer_id)
            if lecturer_data:
                print(f"Welcome, {lecturer_data['name']} from the {lecturer_data['program']} faculty!")
                return lecturer_data
            else:
                print("Error: Lecturer data not found. Please contact admin.")
        else:
            print("Invalid password. Please try again.")


def record_grades(lecturer_data):
    """
    Allows a lecturer to add or update grades for a student in their assigned modules.
    Ensures the student exists in students.txt.
    """
    assigned_modules = [module for module in lecturer_data["modules"] if module != "null"]

    if not assigned_modules:
        print("You do not have any assigned modules to record grades for.")
        return

    print("\nYour Assigned Modules:")
    for module in assigned_modules:
        print(f"- {module}")

    module_code = input("Enter Module Code: ").strip()
    if module_code not in assigned_modules:
        print("Error: You are not authorized to record grades for this module.")
        return

    # Verify student ID against students.txt
    students = read_file(STUDENTS_FILE)
    valid_student_ids = {student.split(",")[0] for student in students}

    while True:
        student_id = input("Enter Student ID: ").strip()
        if student_id not in valid_student_ids:
            print(f"Error: Student ID {student_id} not found in the system. Please try again.")
        else:
            break

    grade = input("Enter Grade (e.g., A, B, C, D, F): ").strip().upper()

    valid_grades = {"A", "B", "C", "D", "F"}
    if grade not in valid_grades:
        print("Invalid grade. Grade must be one of A, B, C, D, or F.")
        return

    # Read the existing grades file
    grades = read_file(GRADES_FILE)
    updated_grades = []
    grade_found = False

    for entry in grades:
        try:
            existing_student_id, existing_module_code, existing_grade = entry.split(",")
            if existing_student_id == student_id and existing_module_code.strip() == module_code:
                print(f"Updating grade for Student {student_id} in Module {module_code} from {existing_grade.strip()} to {grade}.")
                updated_grades.append(f"{student_id},{module_code},{grade}")
                grade_found = True
            else:
                updated_grades.append(entry.strip())
        except ValueError:
            print(f"Skipping malformed entry: {entry}")

    if not grade_found:
        print(f"Adding new grade for Student {student_id} in Module {module_code}: {grade}.")
        updated_grades.append(f"{student_id},{module_code},{grade}")

    # Write the updated grades back to the file
    try:
        with open(GRADES_FILE, "w") as file:
            for updated_entry in updated_grades:
                file.write(updated_entry + "\n")
        print("Grades updated successfully.")
    except Exception as e:
        print(f"Error writing to the grades file: {e}")


def view_student_list_lecturer(course_code):
    """
    Displays the list of students enrolled in a specific course.
    """
    students = read_file(STUDENTS_FILE)
    print(f"\nStudents Enrolled in Course {course_code}:")

    found = False
    for student in students:
        try:
            student_id, name, course, phone, email, gender, dob = student.split(",")
            if course.strip() == course_code:
                print(f"ID: {student_id}, Name: {name}, Phone: {phone}, Email: {email}, Gender: {gender}, DOB: {dob}")
                found = True
        except ValueError:
            print(f"Skipping malformed entry: {student}")

    if not found:
        print(f"No students found for course {course_code}.")


def get_student_by_id(student_id):
    """
    Retrieves details of a specific student by their ID.
    """
    students = read_file(STUDENTS_FILE)
    for student in students:
        try:
            fields = student.split(",")
            if fields[0] == student_id:
                return {
                    "id": fields[0],
                    "name": fields[1],
                    "module": fields[2],
                    "phone": fields[3],
                    "email": fields[4],
                    "gender": fields[5],
                    "dob": fields[6],
                }
        except ValueError:
            print(f"Skipping malformed student entry: {student}")
    print(f"Student with ID {student_id} not found.")
    return None


def track_attendance(lecturer_data):
    """
    Allows a lecturer to mark attendance for students in their assigned modules.
    Ensures the student ID exists in students.txt.
    """
    assigned_modules = [module for module in lecturer_data["modules"] if module != "null"]

    if not assigned_modules:
        print("You do not have any assigned modules to mark attendance for.")
        return

    print("\nYour Assigned Modules:")
    for module in assigned_modules:
        print(f"- {module}")

    module_code = input("Enter Module Code: ").strip()
    if module_code not in assigned_modules:
        print("Error: You are not authorized to mark attendance for this module.")
        return

    # Verify student ID against students.txt
    students = read_file(STUDENTS_FILE)
    valid_student_ids = {student.split(",")[0] for student in students}

    while True:
        student_id = input("Enter Student ID: ").strip()
        if student_id not in valid_student_ids:
            print(f"Error: Student ID {student_id} not found in the system. Please try again.")
        else:
            break

    status = validate_input_lecturer("Enter Attendance (Present/Absent): ", ["Present", "Absent"])

    # Append attendance to the file
    try:
        append_to_file_lecturer(ATTENDANCE_FILE, f"{student_id},{module_code},{status}")
        print(f"Attendance recorded successfully for Student {student_id} in Module {module_code}: {status}.")
    except Exception as e:
        print(f"Error recording attendance: {e}")


def view_student_grades_lecturer():
    """
    Displays grades for all students in a module selected by the lecturer.
    """
    # Display all available modules
    modules = read_file(MODULES_FILE)
    if not modules:
        print("No modules available. Please check the modules file.")
        return

    print("\nAvailable Modules:")
    module_codes = []  # Store valid module codes for validation
    for module in modules:
        try:
            module_code, module_name = module.split(",", 1)
            print(f"- {module_code}: {module_name}")
            module_codes.append(module_code.strip())
        except ValueError:
            print(f"Skipping malformed module entry: {module}")

    # Prompt for valid module code
    while True:
        module_code = input("\nEnter Module Code to view grades: ").strip()
        if module_code not in module_codes:
            print("Invalid module code. Please choose from the available modules.")
        else:
            break

    # Display grades for the selected module
    grades = read_file(GRADES_FILE)
    students = read_file(STUDENTS_FILE)
    print(f"\nGrades for Module {module_code}:")

    found = False
    for grade_entry in grades:
        try:
            student_id, module, grade = grade_entry.split(",")
            if module.strip() == module_code:
                student_name = None
                for student in students:
                    try:
                        student_fields = student.split(",")
                        if student_fields[0] == student_id:
                            student_name = student_fields[1]
                            break
                    except ValueError:
                        continue
                if student_name:
                    print(f"ID: {student_id}, Name: {student_name}, Grade: {grade}")
                else:
                    print(f"ID: {student_id}, Name: [Not Found], Grade: {grade}")
                found = True
        except ValueError:
            print(f"Skipping malformed grade entry: {grade_entry}")

    if not found:
        print(f"No grades found for module {module_code}.")


def update_password_lecturer(lecturer_id):
    """
    Allows a lecturer to update their password in lecturer-account.txt.
    """
    accounts = read_file(LECTURER_ACCOUNT_FILE)
    updated_accounts = []
    password_changed = False

    for acc in accounts:
        fields = acc.strip().split(",")
        if len(fields) == 2 and fields[0] == lecturer_id:
            current_password = fields[1]
            print("Enter your current password to verify:")
            current_password_attempt = input("Current Password: ").strip()
            if current_password_attempt == current_password:
                new_password = input("Enter new password: ").strip()
                confirm_password = input("Confirm new password: ").strip()
                if new_password == confirm_password:
                    updated_accounts.append(f"{lecturer_id},{new_password}")
                    password_changed = True
                    print("Password updated successfully.")
                else:
                    print("Passwords do not match. Password not changed.")
                    updated_accounts.append(acc)  # Keep old password
            else:
                print("Incorrect current password. Password not changed.")
                updated_accounts.append(acc)
        else:
            updated_accounts.append(acc)

    if password_changed:
        # Write updated accounts back to the file
        try:
            with open(LECTURER_ACCOUNT_FILE, "w") as file:
                for account in updated_accounts:
                    file.write(account + "\n")
        except Exception as e:
            print(f"Error updating password file: {e}")


# Lecturer menu
def lecturer_menu(lecturer_data):
    while True:
        print("\nLecturer Menu")
        print("1. View Assigned Modules")
        print("2. Record Grades")
        print("3. View Student List")
        print("4. Track Attendance")
        print("5. View Student Grades")
        print("6. Change Password")
        print("7. Exit")

        choice = validate_input_lecturer("Select an option: ", ["1", "2", "3", "4", "5", "6", "7"])
        if choice == "1":
            view_assigned_modules(lecturer_data["modules"])
        elif choice == "2":
            record_grades(lecturer_data)
        elif choice == "3":
            course_code = input("Enter Course Code: ").strip()
            view_student_list_lecturer(course_code)
        elif choice == "4":
            track_attendance(lecturer_data)
        elif choice == "5":
            view_student_grades_lecturer()  # Ensure no arguments are passed if not needed
        elif choice == "6":
            update_password_lecturer(lecturer_data["id"])
        elif choice == "7":
            print("Exiting Lecturer Menu.")
            break


# Main function
def main_lecturer():
    # Proceed with lecturer login
    lecturer_data = lecturer_login()
    if lecturer_data:
        lecturer_menu(lecturer_data)

if __name__ == "__main__":
    main_lecturer()

# END OF LECTURER MODULE

# START OF STUDENT MODULE

def check_studentmodule_files(): # Look up the contents of the module file and create a file with the name of the module. If it already exists, skip it.
    studentmodules_filepath = "files/modules.txt" # Specifying file path
    try:
        with open(studentmodules_filepath, "r") as f: # Load module file
            modules = f.read().splitlines() # splitlines Separate with a newline character
            modules_n = []
            for module in modules:
                modules_n.append(module[6:])
        txt = ".txt"
        modules_filenames = [original + txt for original in modules_n] #Add .txt to all module names
        modules_filenames = [original.replace(' ', '_') for original in modules_filenames] #Remove all Blank

        for modules_filename in modules_filenames: # Create a file with the name of the module if it does not exist
            modules_filepath = "files/student_modules/" + modules_filename # Creating a file path
            try:
                file = open(modules_filepath, "r") # Try Load the file
                file.close
            except FileNotFoundError: # Create a new file if the file does not exist
                file = open(modules_filepath, "x")
                file.close
        
                
    except FileNotFoundError: #Create the module file if it does not exist
        with open(studentmodules_filepath, "w") as f:
            f.write("")



def check_students_account_file():
    modules_filepath = "files/students_account.txt" # Creating a file path
    try:
        file = open(modules_filepath, "r") # Try Load the file
        file.close
    except FileNotFoundError: # Create a new file if the file does not exist
        file = open(modules_filepath, "x")
        file.close




def show_modules(student_id):
    print("\nHere you can see the available modules\n") 
    print("These are the available modules\n")
    modules_filepath = "files/modules.txt" # Specifying file path
    with open (modules_filepath) as f: # Load and display mudules
        s = f.read()
        print(s)
    module_Edit = input("\n\nIf there is a module you would like to participate in, enter 1 to move to module operations.\nAny other characters entered will return you to the Student menu\n") 
    if module_Edit == "1":
        operate_modules(student_id)
    else:
        student_menu(student_id)




def operate_modules(student_id): #Menu for operations regarding student modules
    print("\nThis is operate modules\nHere you can operate the module\n")
    print("Enter 1 to see the modules you are currently participating in")
    print("Enter 2 to join the new module")
    print("Enter 3 to exit the module you are currently in")
    print("Enter 4 to return to student menu\n")

    while True: #Reject invalid values
        try: ##Input confirmation
            selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
            if selection in [1, 2, 3, 4]:
                break # loop finish
            else:
                print("Enter a number between 1 to 4\n")
        except ValueError:
            print("Enter a number between 1 to 4\n")

    match selection:
        case 1:
            operate_modules_check(student_id)
        case 2:
            operate_modules_join(student_id)
        case 3:
            operate_modules_exit(student_id)
        case 4:
            student_menu()




def check_all_modulefiles():
    file_path = "files/modules.txt"
    all_modules_n = []

    with open(file_path, "r") as f:
        for line in f:
            all_modules_n.append(line[6:].replace(' ', '_').replace('\n',''))

    return all_modules_n



def check_id_in_modulesfiles(student_id):
    all_modules_n = check_all_modulefiles()
    save_specific_file = [] # Store the file containing the specified id

    for file_name in all_modules_n: # Check the contents of each file one by one
        file_path = "files/student_modules/" + file_name + ".txt"
        with open(file_path, 'r') as f:
            for line in f:
                if line[0:5].strip() == student_id: # If the same student ID exists in the file, save the file name
                    save_specific_file.append(file_name)
                    break

    save_specific_file_n = []
    for subject in save_specific_file: # Delete .txt in the file name
        subject = subject.removesuffix('.txt')
        save_specific_file_n.append(subject)
    return save_specific_file_n



def operate_modules_check(student_id): # Displaying modules you are currently participating in
    print("Check the participating modules")
    print("The module you are currently participating in is\n")
    participating_modules = check_id_in_modulesfiles(student_id) # Get information about participating modules
    if participating_modules:
        print(*participating_modules, sep='\n')
    else:
        print("Nothing\nPlease register the module\n")

    print("\nEnter 1 to join the new module")
    print("Enter 2 to exit the module you are currently in")
    print("Enter 3 to return to student menu\n")

    while True: #Reject invalid values
        try: ##Input confirmation
            selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
            if selection in [1, 2, 3]:
                break # loop finish
            else:
                print("Enter a number between 1 to 3\n")
        except ValueError:
            print("Enter a number between 1 to 3\n")

    match selection:
        case 1:
            operate_modules_join(student_id)
        case 2:
            operate_modules_exit(student_id)
        case 3:
            student_menu(student_id)



def operate_modules_join(student_id):
    print("You can join new modules here")
    print("This is the module you can participate in\n")
    all = check_all_modulefiles() # all modules
    Participating = check_id_in_modulesfiles(student_id) # Modules this student is participating in
    # Things that are present in all but not during participation
    unique_to_all = [modules for modules in all if modules not in Participating]
    
    if unique_to_all:
        print(*unique_to_all, sep='\n')

        for module in unique_to_all:
            print(f"\nDo you want to join {module}")
            print("\nEnter 1 to join")
            print("Enter 2 to not join")
            print("Enter 3 to return to student menu\n")
            while True: #Reject invalid values
                try: #Input confirmation
                    selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
                    if selection in [1, 2, 3]:
                        break # loop finish
                    else:
                        print("Enter a number between 1 to 3\n")
                except ValueError:
                    print("Enter a number between 1 to 3\n")

            match selection:
                case 1:
                    file_path = "files/student_modules/" + module + ".txt"
                    with open(file_path, 'a') as f:
                        f.write("\n" + student_id + ",0.00,0.000,0.000")
                    print(f"You participate in {module}")
                case 2:
                    print(f"Did not participate in {module}")
                case 3:
                    student_menu(student_id)
            student_menu(student_id)
        print("\nReturn to student menu")
        student_menu(student_id)

    else:
        print("Nothing\nAlready participated in all modules\n")
        student_menu(student_id)



def operate_modules_exit(student_id):
    print("Here you can remove yourself from the module you are currently participating in\n")
    your_module = check_id_in_modulesfiles(student_id)
    if your_module:
        print(*your_module, sep='\n')

        for module in your_module:
            print(f"\nDo you want to remove {module}")
            print("\nEnter 1 to remove")
            print("Enter 2 to not remove")
            print("Enter 3 to return to student menu\n")
            while True: #Reject invalid values
                try: #Input confirmation
                    selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
                    if selection in [1, 2, 3]:
                        break # loop finish
                    else:
                        print("Enter a number between 1 to 3\n")
                except ValueError:
                    print("Enter a number between 1 to 3\n")

            match selection:
                case 1:
                    file_path = "files/student_modules/" + module + ".txt"
                    new_contents = ""
                    with open(file_path, 'r') as f:
                        for line in f:
                            if line[0:5].strip() == student_id: # Check if the first five characters in the module file are the same as the student ID
                                pass
                            else:
                                new_contents = new_contents + line
                    with open(file_path, 'w') as f:
                        f.write(new_contents)
                    print(f"Removed from {module}")
                case 2:
                    print(f"Did not remove from {module}")
                case 3:
                    student_menu(student_id)
        print("\nReturn to student menu")
        student_menu(student_id)

    else:
        print("Nothing\nyou are not participating in any module\n")
        student_menu(student_id)




def grade(student_id):
    print("\nHere you can see your grade\n")
    print("This is your Grade\n")
    participating_modules = check_id_in_modulesfiles(student_id)
    sum, i = 0, 0
    for module in participating_modules:
        print(module)
        score = check_score(student_id, module)
        print(f"\tScore is {score}")
        classify_grade(score)
        sum += score
        i += 1
    ave = sum / i
    print("Your total grade is")
    classify_grade(ave)
    print("\nReturn to student menu")
    student_menu(student_id)
        


def check_score(student_id, modules):
    file_path = "files/student_modules/" + modules + ".txt"
    with open(file_path, 'r') as f:
        for line in f:
            if line[0:5].strip() == student_id: # If the same student ID exists in the file, save the grade
                grade = float(line[6:10])*100 # Take out the score
                break
    return grade



def classify_grade(score):
    if score >= 90:
        print("\tGrade : A\n")
    elif score >= 80:
        print("\tGrade : B\n")
    elif score >= 70:
        print("\tGrade : C\n")
    elif score >= 60:
        print("\tGrade : D\n")
    elif score >= 50:
        print("\tGrade : E\n")
    else:
        print("\tGrade : F\n")




def attendance(student_id):
    print("Here you can attend your class and your check your attendace percentage\n")
    print("Enter 1 to attend your class")
    print("Enter 2 to check your attendance rate")
    print("Enter 3 to go back student menu")
    while True: #Reject invalid values
        try: #Input confirmation
            selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
            if selection in [1, 2, 3]:
                break # loop finish
            else:
                print("Enter a number between 1 to 3\n")
        except ValueError:
            print("Enter a number between 1 to 3\n")

    match selection:
        case 1:
            attend_class(student_id)
        case 2:
            attendance_check(student_id)
        case 3:
            student_menu(student_id)



def attend_class(student_id): # Attendance confirmation
    result = False
    count = False
    attendance_code = ""
    for i in range(3):
        num = random.randint(0,9)
        attendance_code = attendance_code + str(num)

    print("\n\n**********************************")
    print(f"Assume the attendance code was {attendance_code}")
    print("**********************************\n\n")

    print("Check the participating modules")
    print("The module you are currently participating in is\n")
    participating_modules = check_id_in_modulesfiles(student_id) # Get information about participating modules
    if participating_modules:
        print(*participating_modules, sep='\n')
    else:
        print("Nothing\nYou can not attend any module")
        student_menu(student_id)

    for module in participating_modules:
        if count:
            break
        print(f"\n\nDo you want to attend {module}")
        print("\nEnter 1 to attend this module")
        print("Enter 2 to not attend this module")

        while True: #Reject invalid values
            try: ##Input confirmation
                selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
                if selection in [1, 2]:
                    break # loop finish
                else:
                    print("Enter a number 1 or 2\n")
            except ValueError:
                print("Enter a number 1 or 2\n")

        match selection:
            case 1:
                add_classcount(student_id, module)
                input_num = input("\nPlease enter the 3-digit attendance code: ")
                if input_num == attendance_code:
                    print("\nAttendance Success\n")
                    add_attendance(student_id, module)
                    count = True
                    print("Return to student menu")
                    student_menu(student_id)

                else:
                    print("\nAttendance faild\n")
                    result = True
                    count = True
                    
            case 2:
                print("")
    
    if result:
        print("Would you like to enter again?")
        while True: #Reject invalid values
            try: #Input confirmation
                selection = int(input("Enter 1 to try again\nEnter 2 to go back student menu:  "))
                if selection in [1, 2]:
                    break # loop finish
                else:
                    print("Enter a number between 1 or 2\n")
            except ValueError:
                print("Enter a number between 1 or 2\n")

        match selection:
            case 1:
                attend_class(student_id)
            case 2:
                student_menu(student_id)
                            


def add_attendance(student_id, modules): # Addition of attendance times
    tem_file, num = "", ""
    file_path = "files/student_modules/" + modules + ".txt" # Setting file path
    with open(file_path, 'r') as f: # Reading module files
        for line in f:
            if line[0:5].strip() == student_id: # Check if the first five characters in the module file are the same as the student ID
                num = float(line[11:16])*1000 # Reading attendance count
                num = num + 1 # Add attendance count
                front = line[0:11]
                back = line[16:22]
                num = format(num/1000,'.3f')
                new = front + str(num) + back # Create a string with a new attendance count
            else:
                tem_file = tem_file + (line.strip() + "\n")
        tem_file = tem_file + new
    with open(file_path, 'w') as f:
        f.write(tem_file)



def add_classcount(student_id, modules): # Addition of class times
    tem_file, num = "", ""
    file_path = "files/student_modules/" + modules + ".txt" # Setting file path
    with open(file_path, 'r') as f: # Reading module files
        for line in f:
            if line[0:5].strip() == student_id: # Check if the first five characters in the module file are the same as the student ID
                num = float(line[17:22])*1000 # Reading class count
                num = num + 1 # Add class count
                front = line[0:17]
                num = format(num/1000,'.3f')
                new = front + str(num) # Create a string with a new class count
            else:
                tem_file = tem_file + (line.strip() + "\n")
        tem_file = tem_file + new
    with open(file_path, 'w') as f:
        f.write(tem_file)



def attendance_check(student_id): # Display attendance rate
    print("\n\nThese are your attendance rates\n")
    participating_modules = check_id_in_modulesfiles(student_id) # Get information about participating modules
    i, all_p = 0, 0
    for module in participating_modules:
        i += 1
        file_path = "files/student_modules/" + module + ".txt" # Setting file path
        with open(file_path, 'r') as f: # Reading module files
            for line in f:
                if line[0:5].strip() == student_id: # Check if the first five characters in the module file are the same as the student ID
                    attended = float(line[11:16]) # Reading attended class count
                    all = float(line[17:22]) # Reading all class count
                    try:
                        percent = (attended / all) * 100
                        all_p = all_p + percent
                        print(f"{module} attendance rate is ")
                        print(f"\t--{percent}%--\n")
                        if percent < 70.0: # Display a warning message if the attendance rate is below 70%
                            print("You may fail, Participate in class\n")
                    except ZeroDivisionError: # If the class has never been held
                        print("You have never attended a class yet")
    print(f"\nThe overall attendance rate is\n\t--{all_p/i}%--\n") # Displaying overall attendance rate

    print("Return to student menu")
    student_menu(student_id)




def exit_student(student_id):
    print("Are you sure you want to leave the student module?")
    print("If it's good, enter 'Y'. If it's bad, enter 'N': ")
    while True:
        exit = (input().lower().strip())
        if exit in ["n","y"]:
            break
        else:
            print("Please enter 'Y' or 'N'")
    if exit == 'y':
        print("Return to main menu\n")
        main_menu()
    else:
        print("Continue on student page\n\n")
        student_menu(student_id)



def login_student(): #student login page
    start = False
    print("\nStudent Login Page\n")

    student_id = ""
    while True:
        if len(student_id) == 5:
            break
        else:
            student_id = input("Enter your student ID start with 'S'and must be 5 characters:  ")
    
    student_password = ""
    while True:
        if len(student_password) == 8:
            break
        else:
            student_password = input("Password must be 8 characters:  ")
    student_id, start = check_student_login(student_id, student_password)
    if start:
        check_studentmodule_files()
        check_students_account_file()
        student_menu(student_id)
    else:
        print("Return to main menu")
        main_menu()



def check_student_login(student_id, student_password):#Check if the ID and password match
    student_filepath = "files/students_account.txt" 
    login = False

    try:
        with open(student_filepath, "r") as f:
            students = f.readlines()
        for student in students:
            student_id_C = student[0:5]
            student_password_C = student[6:14]
            if student_id == student_id_C and student_password == student_password_C:
                login = True
                break

        if login:
            print("Login successful\n")
            start = True
            return student_id, start
        else:
            print("Login failed\n") #If login fails, return to main menu or try logging in again
            cont = input("Do you want to continue logging in?\nEnter 1 to continue, any other character will return you to the main menu:  ")
            if cont == "1":
                login_student()
            else:
                print("Return to the main menu")
                main_menu()
                return 00000 , False


    except FileNotFoundError:
        print("Please contact developer")

    



def student_menu(student_id):
    print("==========================")
    print("This is the student module")
    print("==========================\n")
    print("Here you can do various operations for student\n")
    print("Please select the operation you want to do by number\n")
    print("Enter 1 to show all available modules")
    print("Enter 2 to perform operations related to modules")
    print("Enter 3 to view your grades")
    print("Enter 4 to perform operations related to attendance\n")
    print("Enter 5 to go back main menu\n")

    while True: #Reject invalid values
        try:
            selection = int(input("Enter your selection: ").strip()) #.strip() remove unnecessary whitespace
            if selection in [1, 2, 3, 4, 5]:
                break # loop finish
            else:
                print("Enter a number between 1 to 5\n")
        except ValueError:
            print("Enter a number between 1 to 5\n")

    match selection:
        case 1:
            show_modules(student_id)
        case 2:
            operate_modules(student_id)
        case 3:
            grade(student_id)
        case 4:
            attendance(student_id)
        case 5:
            exit_student()

# END OF STUDENT MENU

main_menu()
