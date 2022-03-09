def prime_numbers_range(lower, upper):
    """
    Prime numbers in a given range - lower to upper.
    :param lower: lower value of given range
    :param upper: upper value of given range
    :return: A list of prime numbers in given range
    """
    try:
        prime_nos = []
        # Traversing though the range
        for num in range(lower, upper + 1):
            # Checking if every number is divisible by their previous all the numbers
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    prime_nos.append(num)
        return my_list
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        lower = int(input("Enter a lower limit: "))
        upper = int(input("Enter an upper limit: "))
        print(prime_numbers_range(0, 1000))
        # print(prime_numbers_range(lower, upper))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
