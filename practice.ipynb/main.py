def get_marks():
    marks = []
    for i in range(5):
        mark = int(input("Enter mark for subject: "))
        marks.append(mark)
    return marks

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return (total / 500) * 100

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "F"

def display_result(name, total, percentage, grade):
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def main():
    name = input("Enter name: ")

    marks = get_marks()
    total = calculate_total(marks)
    percentage = calculate_percentage(total)
    grade = get_grade(percentage)

    display_result(name, total, percentage, grade)

main()