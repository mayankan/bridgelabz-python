def prime_numbers_range(lower, upper):
    """Prime numbers in a given range
    Parameters:
        lower: lower value of that range
        upper: upper value of the range
    Returns:
        A list of prime numbers in that range
    """
    print("Prime numbers between ", lower, " and ", upper, " are: ")

    my_list = []
    # Traversing though the range
    for num in range(lower, upper + 1):
        # Checking if every number is divisible by their previous all the numbers
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                my_list.append(num)
    print(my_list)


def main():
    lower = int(input("Enter a lower limit: "))
    upper = int(input("Enter an upper limit: "))
    prime_numbers_range(lower, upper)


if __name__ == "__main__":
    main()
