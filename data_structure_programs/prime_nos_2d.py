def print_prime(hi, lo):
    """
    Return a list of prime numbers between the specified range
    [2, 3, 5, 7]
    """
    prime_lis = []
    for num in range(hi, lo):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_lis.append(num)
    return prime_lis


def range_prime_generation():
    # Function to generate prime number in a ranges of 100 starting from 0 to 1000
    """ Function to return prime number in ranges """
    new_array = []
    for i in range(0, 1000, 100):
        prim_num = print_prime(i, i + 100)
        new_array.append(prim_num)
    prime_printing(new_array)
    return


def prime_printing(new_array):
    """
    Function to print prime number in a ranges
    :param new_array:
    :return:
    """
    i = 0
    for j in range(0, 1000, 100):
        print("The prime numbers in the range {} to {} is :".format(j, j + 100))
        print(new_array[i])
        i += 1
    return


def main():
    range_prime_generation()


if __name__ == "__main__":
    main()
