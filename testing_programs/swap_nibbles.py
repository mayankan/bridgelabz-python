# Importing Util Class from Decimal_to_Binary file for Conversion to Binary Representation.
from decimal_to_binary import Util


# Function for swap nibble
def swap_nibbles(number):
    """
    Swapping the two nibbles, i.e. binary representation 01100100 for decimal number 100 having (0110) and (0100)
    swapped to 01000110.
    :param number: binary representation of decimal number.
    :return: binary number after swapping nibbles.
    """
    return number[4:9] + number[0:4]


def main():
    try:
        number = int(input("Enter a decimal number to swap value: "))
        # Converting Decimal to Binary Representation using Util Class Decimal_to_Binary Function in other file.
        binary_number = Util().decimal_to_binary(number)
        swapped_number = swap_nibbles(binary_number)
        print("Resultant number after swapping nibbles is {}".format(swapped_number))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
