
# Number Guessing Game

# importing Numpy to generate random number
import numpy as np

# Function to guess lucky number


def guess(num, lower_limit, upper_limit):
    num1 = np.random.randint(lower_limit, upper_limit)

    while True:
        if num != num1:
            num = int(input("Try again: "))
        if num == num1:
            print("Congrats you did it.")
            break

# Function to get limits and user num


def user_input():
    try:
        lower_limit = int(input("Give your lower limit: "))
        upper_limit = int(input("Give your upper limit: "))
        num = int(input("Give your lucky num: "))
        guess(num, lower_limit, upper_limit)
    except Exception as e:
        print(e)


user_input()
