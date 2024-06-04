def get_letter_grade(numeric_grade):
    if numeric_grade >= 90 and numeric_grade <= 100:
        return "A"
    elif numeric_grade >= 80 and numeric_grade < 90:
        return "B"
    elif numeric_grade >= 70 and numeric_grade < 80:
        return "C"
    elif numeric_grade >= 60 and numeric_grade < 70:
        return "D"
    elif numeric_grade >= 0 and numeric_grade < 60:
        return "F"
    else:
        return None

# Input a numeric grade from the user
numeric_grade = float(input("Enter the numeric grade: "))

# Check if the numeric grade is within the range
if numeric_grade >= 0 and numeric_grade <= 100:
    # letter grade
    letter_grade = get_letter_grade(numeric_grade)
    # Print letter grade
    print("The letter grade is:", letter_grade)
else:
    print("Error: Grade must be between 0 and 100.")
