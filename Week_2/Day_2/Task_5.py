# Create a program that checks if a given string can be rearranged to form a palindromic string.

"""A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward.
Ask the user to input a string.
Check and print whether the given string can be rearranged to form a palindrome.
Ignore spaces and consider the characters in a case-insensitive manner.
Handle cases where the input is empty or contains non-alphabetic characters."""


def palindrome_check(data):
    NO_OF_CHARS = 256

    count = [0 for i in range(NO_OF_CHARS)]

    for i in data:
        count[ord(i)] += 1

    odd = 0
    for i in range(NO_OF_CHARS):
        if (count[i] & 1):
            odd += 1

        if (odd > 1):
            return False
    return True


data = str(input("Give any word: "))

palindrome_check(data)

if data:
    print("Palindrome")
else:
    print("Not Palindrome")
