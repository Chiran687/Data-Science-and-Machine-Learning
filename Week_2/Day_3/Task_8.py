
# Prime Factorization

# Find Factors of number
def get_prime(num):
    x = [0 for i in range(num+1)]
    x[1] = 1
    for i in range(2, num+1):
        x[i] = i
    for i in range(4, num+1, 2):
        x[i] = 2

    for i in range(3, int(num**0.5)+1):
        if x[i] == i:
            for j in range(i*i, num+1, i):
                if x[j] == j:
                    x[j] = i

    while num != 1:
        print(x[num], end=" ")
        num = num // x[num]

# Main Function to take user input


def main():
    try:
        num = int(input("Give your num: "))
    except Exception as e:
        print(e)
    # pass number to get_prime function
    get_prime(num)


main()
