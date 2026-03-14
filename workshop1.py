students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Records:")
        for s in students:
            print("Name:", s["Name"], "| Roll:", s["Roll"], "| Marks:", s["Marks"])
        print()


def search_student():
    roll = input("Enter roll number to search: ")

    for s in students:
        if s["Roll"] == roll:
            print("Student Found:")
            print("Name:", s["Name"])
            print("Roll:", s["Roll"])
            print("Marks:", s["Marks"])
            return

    print("Student not found.\n")


while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.\n")