def calc_harmonic_no(harmonic_limit):
    """
    Calculates the n-th Harmonic number(1/1 + 1/2 + .. + 1/n) till the given number limit.
    :param harmonic_limit: limit till which n-th harmonic number is calculated.
    :return: n-th harmonic number, i.e. sum of the reciprocals of the first n natural numbers.
    """
    harmonic_no = 0
    for index in range(1, harmonic_limit+1):
        harmonic_no = harmonic_no + 1 / index
    return harmonic_no


def main():
    harmonic_limit = 0
    while harmonic_limit == 0:
        harmonic_limit = int(input("Enter the number till which you want to print harmonic number: "))
    print(calc_harmonic_no(harmonic_limit))


if __name__ == "__main__":
    main()
