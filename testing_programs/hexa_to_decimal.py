DECOMPOSITION_TABLE = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hexa_to_decimal(hexadecimal):
    """
    Converts Hexadecimal number to Decimal Number by multiplying 16^n to each value as per position.
    :param hexadecimal: Hexadecimal number provided by user.
    :return: Number converted to Decimal Number by multiplying 16^n to each value as per position.
    """
    try:
        decimal = 0
        n = len(hexadecimal) - 1
        # Powers of 2 in decreasing order
        for index in hexadecimal:
            if index in DECOMPOSITION_TABLE:
                decimal += int(DECOMPOSITION_TABLE[index]) * (16 ** n)
            else:
                decimal += (int(index) * (16 ** n))
            n -= 1
        return decimal
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    try:
        hexadecimal = input("Enter a hexadecimal number: ")
        number = hexa_to_decimal(hexadecimal)
        print("Decimal representation of Hexadecimal number {}: {}".format(hexadecimal, number))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
