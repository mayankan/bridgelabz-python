def check_leap_year(input_no):
    """
    Checks whether the number is leap year or not.
    :param input_no: input number to check if it is leap year.
    :return: 1 if the number is leap year else 0.
    """
    if input_no % 400 == 0 or input_no % 4 == 0 and input_no % 100 != 0:
        return 1
    else:
        return 0


def main():
    input_no = 0
    while len(str(input_no)) != 4:
        input_no = int(input("Enter a four digit number to check it is leap year: "))
    print("Input is a leap year." if check_leap_year(input_no) == 1 else "Input is not a leap year.")


if __name__ == "__main__":
    main()
