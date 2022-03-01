def pow_of_2(power_limit):
    """
    Generates a list of values that are power of 2 starting from 1 to the given number.
    :param power_limit: Given number till which the power of 2 is calculated.
    :return: List of values containing power of 2 starting from 1 to given number.
    """
    output_list = []
    for index in range(1, power_limit+1):
        output_list.append(2 ** index)
    return output_list


def main():
    power_limit = 35
    while power_limit >= 31 or power_limit < 0:
        power_limit = int(input("Enter the root of number till which you want to print power of 2: "))
    print(*pow_of_2(power_limit), sep="\n")


if __name__ == "__main__":
    main()
