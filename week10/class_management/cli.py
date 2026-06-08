from class_management.service import ClassManager


def print_menu() -> None:
    print("\nClass Management System")
    print("1. Add student")
    print("2. Add course")
    print("3. Enroll student in course")
    print("4. Mark attendance")
    print("5. Add grade")
    print("6. View students")
    print("7. View courses")
    print("8. View enrollments")
    print("9. Exit")


def run() -> None:
    manager = ClassManager()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            email = input("Email: ").strip()
            success = manager.add_student(student_id, name, age, email)
            print("Student added." if success else "Student ID already exists.")

        elif choice == "2":
            course_id = input("Course ID: ").strip()
            title = input("Course title: ").strip()
            teacher = input("Teacher name: ").strip()
            success = manager.add_course(course_id, title, teacher)
            print("Course added." if success else "Course ID already exists.")

        elif choice == "3":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()
            success = manager.enroll_student(student_id, course_id)
            print("Enrollment created." if success else "Enrollment failed.")

        elif choice == "4":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            success = manager.mark_attendance(student_id, course_id, date)
            print("Attendance marked." if success else "Enrollment not found.")

        elif choice == "5":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()
            grade = float(input("Grade: ").strip())
            success = manager.add_grade(student_id, course_id, grade)
            print("Grade added." if success else "Enrollment not found.")

        elif choice == "6":
            students = manager.get_students()
            if not students:
                print("No students found.")
            for student in students:
                print(student)

        elif choice == "7":
            courses = manager.get_courses()
            if not courses:
                print("No courses found.")
            for course in courses:
                print(course)

        elif choice == "8":
            enrollments = manager.get_enrollments()
            if not enrollments:
                print("No enrollments found.")
            for enrollment in enrollments:
                print(enrollment)

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Try again.")
