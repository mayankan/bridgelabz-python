def euclidean_distance(x, y):
    try:
        distance = (x * x + y * y) ** 1 / 2
        return distance
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        x = int(input("Enter value representing x axis of a point: "))
        y = int(input("Enter value representing y axis of a point: "))
        print("Distance between this point and 0 is {}".format(euclidean_distance(x, y)))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
