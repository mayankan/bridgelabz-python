CONVERSION_TABLE = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
DECOMPOSITION_TABLE = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


class Util:
    @staticmethod
    def decimal_to_hexa(number):
        """
        Converts Decimal number to Hexadecimal Number by using quotient and remainder values after division by 16.
        :param number: Decimal number, i.e. an integer provided by user.
        :return: Number converted to Hexadecimal number by using quotient and remainder values after division by 16.
        """
        hexadecimal = ""  # Converting the number into a string
        while number > 0:
            remainder = number % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = CONVERSION_TABLE[remainder] + hexadecimal
            number = number // 16
        return hexadecimal

    @staticmethod
    def hexa_decomposition(hexadecimal):
        """
        Decomposes hexadecimal value, i.e. interpretation for each 1 value in a hexadecimal number.
        :param hexadecimal: Hexadecimal value used to decompose.
        :return: List having Hexadecimal Decomposed values.
        """
        decomposed_values = []
        n = len(hexadecimal) - 1
        # Powers of 2 in decreasing order
        for index in hexadecimal:
            if index in DECOMPOSITION_TABLE:
                decomposed_values.append(int(DECOMPOSITION_TABLE[index]) * (16 ** n))
            else:
                decomposed_values.append(int(index) * (16 ** n))
            n -= 1
        return decomposed_values


def main():
    try:
        number = int(input("Enter a number: "))
        decimal_hexa_instance = Util()
        hexadecimal = decimal_hexa_instance.decimal_to_hexa(number)
        print("Hexadecimal representation of {}: {}".format(number, hexadecimal))
        hexa_decomposed = decimal_hexa_instance.hexa_decomposition(hexadecimal)
        print("Hexadecimal Decomposition of {}: {}".format(hexadecimal, hexa_decomposed))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
