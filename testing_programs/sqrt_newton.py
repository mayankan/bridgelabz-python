class Util:
    @staticmethod
    def sqrt_newton(c):
        """
        Calculates Square Root of the given non-negative number by user using Newton's method.
        :param c: non-negative number provided by the user.
        :return: square root of given number calculated using newton's method.
        """
        try:
            epsilon = 1e-15
            t = c
            # repeating until the desired accuracy is reached
            while abs(t - c / t) > epsilon * t:
                t = (c / t + t) / 2
            return t
        except Exception as e:
            print("{} is raised.".format(str(e)))


def main():
    try:
        c = abs(int(input("Enter a non negative number: ")))
        sqrt_instance = Util()
        square_root = sqrt_instance.sqrt_newton(c)
        print("Square root of non negative number {} is {}".format(c, square_root))
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
