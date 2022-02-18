def calculate_line_length(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    length_of_point = (x * x + y * y) ** 1/2
    return length_of_point


def check_line_length(_x1, _y1, _x2, _y2):
    """

    :param _x1:
    :param _y1:
    :param _x2:
    :param _y2:
    :return:
    """
    length_of_point1 = (_x1 * _x1 + _y1 * _y1) ** 1 / 2
    length_of_point2 = (_x2 * _x2 + _y2 * _y2) ** 1 / 2
    if length_of_point1 == length_of_point2:
        return 1
    else:
        return 0


def compare_line_length(_x1, _y1, _x2, _y2):
    """

    :param _x1:
    :param _y1:
    :param _x2:
    :param _y2:
    :return:
    """
    length_of_point1 = (_x1 * _x1 + _y1 * _y1) ** 1 / 2
    length_of_point2 = (_x2 * _x2 + _y2 * _y2) ** 1 / 2
    if length_of_point1 > length_of_point2:
        return 1
    elif length_of_point1 < length_of_point2:
        return 2
    else:
        return 0


def main():
    print("Welcome to Line Comparison Computation ")
    x1 = int(input("Enter x-axis coordinate of a point: "))
    y1 = int(input("Enter y-axis coordinate of a point: "))
    x2 = int(input("Enter x-axis coordinate of another point: "))
    y2 = int(input("Enter y-axis coordinate of another point: "))
    print("Length of Line One is {}".format(calculate_line_length(x1, y1)))
    print("Length of Line Two is {}".format(calculate_line_length(x2, y2)))
    print("Line One is equal to Line Two") if check_line_length(x1, y1, x2, y2) == 1 else print("Line One is not "
                                                                                                "equal to Line Two")
    line_comparison = compare_line_length(x1, y1, x2, y2)
    if line_comparison == 1:
        print("Line One is greater than Line Two")
    elif line_comparison == 2:
        print("Line Two is greater than Line One")
    else:
        print("Line One is equal to Line Two")


if __name__ == "__main__":
    main()

