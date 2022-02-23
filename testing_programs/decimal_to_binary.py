class Util:
    @staticmethod
    def decimal_to_binary(number):
        """
        Converts Decimal number to Binary Number by using quotient and remainder values after division by 2.
        :param number: Decimal number, i.e. an integer provided by user.
        :return: Number converted to Binary number by using quotient and remainder values after division by 2.
        """
        try:
            binary = ""  # Converting the number into a string
            while number:
                remainder = number % 2
                number = number // 2
                # Printing out the remainder while continuously dividing the number by 2
                binary += str(remainder)
            # Reversing the remainder string and printing it out
            reverse_binary = binary[::-1]
            # Makes the Binary number an eight digit representation.
            if len(reverse_binary) < 8:
                zeros = "0" * (8-len(reverse_binary))
                reverse_binary = zeros + reverse_binary
            return reverse_binary
        except Exception as e:
            print("{} is raised.".format(str(e)))

    @staticmethod
    def binary_decomposition(binary):
        """
        Decomposes binary value, i.e. interpretation for each 1 value in a binary number.
        :param binary: Binary value used to decompose.
        :return: List having binary Decomposed values.
        """
        try:
            decomposed_values = []
            n = len(binary) - 1
            # Powers of 2 in decreasing order
            for index in binary:
                if index != "0":
                    decomposed_values.append(int(index) * (2 ** n))
                n -= 1
            return decomposed_values
        except Exception as e:
            print("{} is raised.".format(str(e)))


def main():
    try:
        number = int(input("Enter a number: "))
        decimal_binary_instance = Util()
        binary_number = decimal_binary_instance.decimal_to_binary(number)
        print("Binary representation of {}: {}".format(number, binary_number))
        binary_decomposed = decimal_binary_instance.binary_decomposition(binary_number)
        print("Binary Decomposition of {}: {}".format(binary_number, binary_decomposed))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
