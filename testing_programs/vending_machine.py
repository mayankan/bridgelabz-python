def vending_machine(amount):
    """
    Prints the least number of currency notes available for the given amount.
    :param amount: Total Amount entered by the user.
    :return: Printing each currency starting from 1000 and going as least as 1.
    """
    try:
        while amount > 0:  # todo
            if amount >= 1000:
                a = amount // 1000
                print("1000 X {}".format(a))
                amount = amount - (1000 * a)  # Calculating the remaining amount

            elif amount >= 500:
                a = amount // 500
                print("500 X {}".format(a))
                amount = amount - (500 * a)

            elif amount >= 100:
                a = amount // 100
                print("100 X {}".format(a))
                amount = amount - (100 * a)

            elif amount >= 50:
                a = amount // 50
                print("50 X {}".format(a))
                amount = amount - (50 * a)

            elif amount >= 10:
                a = amount // 10
                print("10 X {}".format(a))
                amount = amount - (10 * a)

            elif amount >= 5:
                a = amount // 5
                print("5 X {}".format(a))
                amount = amount - (5 * a)

            elif amount >= 2:
                a = amount // 2
                print("2 X {}".format(a))
                amount = amount - (2 * a)

            else:
                a = amount // 1
                print("1 X {}".format(a))
                amount = amount - (1 * a)
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    try:
        amount = int(input("Enter the amount: "))
        vending_machine(amount)
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
