import datetime
from datetime import *


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
            login_success()
        else:
            print("PW Wrong")
            login_fail()
    else:
        login_fail()


def login_success():  # Shows success message and sends user to the main admin menu
    print("")
    print("Admin login successful!")
    print("")

    admin_menu()


def login_fail():  # Gives the user options to try again or to choose their account type again.
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

        target_course_code = ""  # Gets the course code that the user wants to delete
        while True:
            try:
                if len(target_course_code) != 5 or target_course_code not in available_course_codes:  # Length and existence check
                    if target_course_code == 'exit':  # Option for user to cancel the deletion process
                        manage_courses_menu()
                    if len(available_course_codes) == 0:  # If there are no courses, user cannot delete anything
                        print("")
                        print("There are no courses yet! You need to create a course before deleting one.")
                        print("")
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
                        course_code, course_name, course_credits, sem_1, sem_2, sem_3, sem_4, sem_5, sem_6 = course.split(',')
                        print(f"Course Code: {course_code}")
                        print(f"Course Name: {course_name}")
                        print(f"Course Credits: {course_credits}")
                        print(f"Semester 1 Fees: ${sem_1}")
                        print(f"Semester 2 Fees: ${sem_2}")
                        print(f"Semester 3 Fees: ${sem_3}")
                        print(f"Semester 4 Fees: ${sem_4}")
                        print(f"Semester 5 Fees: ${sem_5}")
                        print(f"Semester 6 Fees: ${sem_6}")
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
            if '@' and '.' not in new_email:  # Length and uniqueness check for course code
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
                        if len(available_faculty_code) == 0:
                            print("You need to create a faculty first before registering a lecturer!")
                            admin_menu()
                        lecturer_faculty_code = input("Lecturer Faculty Code (2 characters and exists): ")
                    else:
                        break
                except ValueError:
                    pass

            while True:  # Repeats infinitely unless a valid choice is given
                try:
                    number_of_modules = int(input(
                        "Enter number of modules this lecturer is in-charge of (1/2/3/4): "))  # Gets the user's input
                    if number_of_modules in range(1, 5):  # Checks if the user input is valid
                        break  # Stops the while loop
                    else:
                        print("You need to enter a value between 1 and 4!")
                        print("")
                except ValueError:  # Exception handling in case a non-integer value is inputted
                    print("You need to enter a value between 1 and 4!")
                    print("")
            try:
                with open(modules_filepath, "r") as file2:
                    modules = file2.readlines()
                    existing_module_codes = []
                    for module in modules:
                        existing_module_codes.append(module[0:5])
                        print(existing_module_codes)
            except FileNotFoundError:
                print("An error has occurred! The file was not found. Please contact developer.")

            lecturer_modules = ["null"] * 4
            for i in range(number_of_modules):
                module_code = ""
                while True:
                    try:
                        if len(module_code) != 5 or module_code not in existing_module_codes:
                            if len(existing_module_codes) == 0:
                                print("There are currently no modules available right now!")
                                manage_lecturers_menu()
                            module_code = input("Module Code (5 characters and unique): ")
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

        target_lecturer_id = ""
        while True:
            try:
                if len(target_lecturer_id) != 4 or target_lecturer_id not in available_lecturer_ids:
                    if target_lecturer_id == 'exit':
                        manage_lecturers_menu()
                    if len(available_lecturer_ids) == 0:
                        print("")
                        print(
                            "There are no lecturers registered yet! Create one before you delete one.")
                        print("")
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

    print("======================")
    print("Generated Admin Report")
    print("======================")
    print("")
    print(f"| Total Registered Students: {total_students}")
    print(f"| Total Active Courses: {total_courses}")
    print(f"| Total Registered Modules: {total_modules}")
    print(f"| Total Faculties: {total_faculties}")
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
    check_backup_date()
    check_student_account_file()
    check_lecturer_account_file()

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
            login_registar()  # Login page for Registrar
        case 5:
            login_accountant()  # Login page for accountants
        case 6:
            exit()  # Exits the program


main_menu()
