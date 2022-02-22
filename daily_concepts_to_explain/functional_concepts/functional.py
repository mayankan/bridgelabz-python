from functools import reduce


def add(x, y):
    return x + y


FRUITS = ["Apple", "Banana", "Pear", "Apricot", "Orange"]


def map_function():
    map_object = map(lambda s: s[0] == "a", FRUITS)
    return list(map_object)


def filter_function():
    filter_object = filter(lambda s: s[0] == "A", FRUITS)
    return list(filter_object)


def reduce_function():
    return reduce(lambda x, y: x + y, FRUITS)


def main():
    print(add(2, 3))
    # sum_function = lambda x, y: x + y  # Using Lambda Function
    # print(sum_function(2, 3))
    print(map_function())
    print(filter_function())
    print(reduce_function())


if __name__ == "__main__":
    main()
