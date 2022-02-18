def euclidean_distance(x, y):
    distance = (x * x + y * y) ** 1 / 2
    return distance


def main():
    x = int(input("Enter value representing x axis of a point: "))
    y = int(input("Enter value representing y axis of a point: "))
    print("Distance between this point and 0 is {}".format(euclidean_distance(x, y)))


if __name__ == "__main__":
    main()
