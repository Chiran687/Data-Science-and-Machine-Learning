# Create a program that calculates the ticket price
# for a movie based on the age and whether the customer is a student.

"""Get the user's age and whether they are a student (True or False) as input.
Define the ticket prices:
Children (age 0-12): $10
Teenagers (age 13-17): $15
Adults (age 18 and above): $20
Students (regardless of age): $18 (discounted price)
Calculate and print the ticket price based on the user's age and student status.
Handle cases where the entered age is not a valid numeric value.
Provide a message for cases where the age is negative or non-integer."""


def ticket_price(student, age):

    if student == "y" and "Y":
        if age >= 0 and age < 12:
            print("Price is $10")
        elif age > 13 and age < 17:
            print("Price is $15")
        elif age > 18:
            print("Price is $20")
        else:
            print("invalid age")
    elif student == "n" and "N":
        print("Unable to provide student discount")
    else:
        print("Invalid command")
        print("Unable to provide student discount")


def User_Input():

    student = str(
        input("Please type y if you are student, n if you are not student"))

    age = int(input("Please give age: "))

    ticket_price(student, age)


User_Input()
