# Create a simple grading system where a student's score is entered,
# and the program determines the corresponding grade.

def grade_calculation(marks):

    if marks > 90 and marks < 100:
        print("The grade is A")
    elif marks > 80 and marks < 89:
        print("The grade is B")
    elif marks > 70 and marks < 79:
        print("The grade is C")
    elif marks > 60 and marks < 69:
        print("The grade is C")
    elif marks >= 0 and marks < 60:
        print("The grade is F")
    else:
        print("Please Double check your marks")


marks = float(input("Give Number of Student: "))
grade_calculation(marks)
