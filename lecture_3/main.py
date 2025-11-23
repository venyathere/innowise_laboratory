import re

students = []

def add_student():
    while True:
        grades_list = []
        student_name = input("Enter student name: ")
        pattern = r'[\d\W]'
        check_for_digits_and_spec_chars = bool(re.search(pattern, student_name))
        if check_for_digits_and_spec_chars == True:
            print("Digits and special characters aren't allowed in names. Please, try again.")
            continue
        else:
            students.append({'Name': student_name, 'Grades': grades_list})
            print(f"Student {student_name} was added succesfully!")
            break


def add_grades():
    grades_list = []
    while True:
        grades_input = input("Enter student's grade or type 'done' to finish: ").lower()
        try:
            if grades_input == "done":
                break
            elif int(grades_input) is True:
                continue
            else:
                while int(grades_input) >0 and int(grades_input) <= 100:
                    grades_list.append(int(grades_input))
                    break
                else:
                    print("The grade should be  in range from 0 to 100")
                continue
            
        except ValueError:
            print("Only digits are allowed. Please, try again.")
    return grades_list

def show_report():
    print("Here is your report")
    print("#   Name        Grades         Average")
    count = []
    for student in students:
        try:
            avg = round(sum(student['Grades']) / len(student['Grades']), 2)
        except TypeError:
            avg = 0
        except ZeroDivisionError:
            avg = 0
        student_name = student['Name']
        grades = student['Grades']
        student["Average"] = avg
        count.append(1)
        print(f"{len(count)}.   {student_name}        {grades}         {avg}")
    
    print("---------------------------")
    max_avg = max(map(lambda x: x["Average"], students))
    min_avg = min(map(lambda x: x["Average"], students))
    overall = list(map(lambda x: x["Average"], students))
    overall_avg = round(sum(overall) / len(overall), 2)
    print(f"Maximum average is {max_avg}")
    print(f"Minumum average is {min_avg}")
    print(f"Overall average is {overall_avg}")

def show_top():
    if len(students) == 0:
        print("No students. Please, add students.")
    else:
        for student in students:
            try:
                avg = round(sum(student['Grades']) / len(student['Grades']), 2)
            except TypeError:
                avg = 0
            except ZeroDivisionError:
                avg = 0
            student_name = student['Name']
            grades = student['Grades']
            student["Average"] = avg
            max_avg = max(map(lambda x: x["Average"], students))
        for student in students:
            if student["Average"] == max_avg:
                print(f"Student with highest average grade of {max_avg} is {student["Name"]}")
            else:
                continue
def main():
    while True:
        print("--- Student grade analyzer ---")
        print("1. Add a student")
        print("2. Add grades for a student")
        print("3. Generate full report")
        print("4. Find top student")
        print("5. Exit program")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                add_student()

            if choice == 2:
                student_name = input("Enter a student name: ")
                for i in range(len(students)):
                    if students[i]['Name'].lower() != student_name.lower():
                        if i < len(students):
                            continue
                        else:
                            print("x123")
                        break
                    else:
                        grades_list = add_grades()
                        for grade in grades_list:
                            students[i]['Grades'].append(grade)
                        break
                        
            if choice == 3:
                show_report()

            if choice == 4:
                show_top()

            if choice == 5:
                break

            if choice > 5:
                print("Incorrect choice. Please, try again.")
        except ValueError:
            print("Incorrect choice. Please, try again.")

main()