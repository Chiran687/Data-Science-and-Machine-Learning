# Create a program that analyzes a given text and counts the frequency of each unique word.

"""Ask the user to input a paragraph or sentence.
Tokenize the input into words (ignoring punctuation and case sensitivity).
Count the frequency of each unique word.
Display the word frequencies in alphabetical order.
Handle cases where the input is empty."""


def frequency_calc(data):
    result = {key: data.split(" ").count(key) for key in data.split(" ")}
    for x, i in enumerate(sorted(result.items())):
        print(x, str(i))


data = str(input("Give you paragraph to parse: "))
frequency_calc(data)
