def quadratic_equation(a, b, c):
    """
    Return roots of the quadratic equation, i.e. a*x*x+b*x+c.
    :param a: first variable in the quadratic equation.
    :param b: second variable in the quadratic equation.
    :param c: third variable in the quadratic equation.
    :return: list of two roots of the quadratic equation.
    """
    delta = b*b - 4*a*c
    root1 = (-b + (delta ** 1/2)) / (2 * a)
    root2 = (-b - (delta ** 1/2)) / (2 * a)
    return [root1, root2]


def main():
    a = int(input("Enter first variable to find roots of the quadratic equation: "))
    b = int(input("Enter second variable to find roots of the quadratic equation: "))
    c = int(input("Enter third variable to find roots of the quadratic equation: "))
    roots = quadratic_equation(a, b, c)
    print("Roots of the above quadratic equation {0}*x^2+{1}*x+{2} are: ".format(a, b, c))
    print(*roots, sep=', ')


if __name__ == "__main__":
    main()
