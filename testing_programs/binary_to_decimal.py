def binary_to_decimal(binary):
    """
    Converts Binary number to Decimal Number by multiplying 2^n to each value as per position.
    :param binary: Binary number provided by user.
    :return: Number converted to Decimal Number by multiplying 2^n to each value as per position.
    """
    try:
        decimal = 0
        n = len(binary) - 1
        # Powers of 2 in decreasing order
        for index in binary:
            if index != "0":
                decimal += int(index) * (2 ** n)
            n -= 1
        return decimal
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    try:
        binary = input("Enter a binary number: ")
        number = binary_to_decimal(binary)
        print("Decimal representation of Binary number {}: {}".format(binary, number))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
