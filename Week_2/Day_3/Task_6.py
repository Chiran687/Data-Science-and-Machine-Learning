# Word Pyramid Generator

def pyramid(data, prompt):
    word_length = len(data)

    # Generate the pyramid
    if prompt == 1:

        for i in range(word_length):
            spaces = " " * (word_length - i - 1)
            letters = " ".join(data[:i+1])
            print(spaces + letters)

    if prompt == 0:
        for i in range(word_length):
            spaces = " " * i
            letters = " ".join(data[:word_length-i])
            print(spaces + letters)

    elif prompt != 1 and prompt != 1:
        print("Invalid Command")

# take User input


def main():
    data = str(input("Enter a word: "))
    prompt = int(input("Enter 1 for upward pyramid and 0 for downward: "))
    pyramid(data, prompt)


main()
