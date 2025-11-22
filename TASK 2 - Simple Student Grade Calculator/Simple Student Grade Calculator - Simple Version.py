def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(total):
    return total / 3

def calculate_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Main program
name = input("Enter student's name: ")
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = calculate_total(subject1, subject2, subject3)
average = calculate_average(total)
grade = calculate_grade(average)

print("\n------ Student Result ------")
print(f"Student Name : {name}")
print(f"Total Marks  : {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade        : {grade}")
print("----------------------------")
