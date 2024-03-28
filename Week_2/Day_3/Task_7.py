
# List Manipulation - Odd-Even Sorter

# Function to check Odd or Even
def odd_even(parsed_num):
    odd_list = []
    even_list = []
    # validation Process
    for i in parsed_num:
        if i % 2 == 0:
            even_list.append(i)
    for i in parsed_num:
        if i % 2 == 1:
            odd_list.append(i)

    # Printing
    if even_list:
        print(f"The even are {even_list} ")
    else:
        print("There are no even Numbers.")

    if odd_list:
        print(f"The odd are {odd_list} ")
    else:
        print("There are no odd Numbers")

# Function to parse and filter user input


def parse(num):
    parsed_num = []
    for i in num.split(","):
        parsed_num.append(int(i))
    odd_even(parsed_num)

# take user input and pass to parse


def main():
    num = input("Give num seperated by comma: ")
    parse(num)


main()
