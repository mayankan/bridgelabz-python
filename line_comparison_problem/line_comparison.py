
print("Welcome to Line Comparison Computation ")

x1 = int(input("Enter x-axis coordinate of a point: "))
y1 = int(input("Enter y-axis coordinate of a point: "))
x2 = int(input("Enter x-axis coordinate of another point: "))
y2 = int(input("Enter y-axis coordinate of another point: "))


def calculate_line_length(x, y):
    length_of_point = (x * x + y * y) ** 1/2
    return length_of_point


def check_line_length(_x1, _y1, _x2, _y2):
    length_of_point1 = (_x1 * _x1 + _y1 * _y1) ** 1 / 2
    length_of_point2 = (_x2 * _x2 + _y2 * _y2) ** 1 / 2
    if length_of_point1 == length_of_point2:
        return 1
    else:
        return 0


def compare_line_length(_x1, _y1, _x2, _y2):
    length_of_point1 = (_x1 * _x1 + _y1 * _y1) ** 1 / 2
    length_of_point2 = (_x2 * _x2 + _y2 * _y2) ** 1 / 2
    if length_of_point1 > length_of_point2:
        return 1
    elif length_of_point1 < length_of_point2:
        return 2
    else:
        return 0

