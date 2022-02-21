def print_matrix(matrix):
    """
    Prints 2 Dimensional Matrix values individually.
    :param matrix: list of list having 2 Dimensional matrix values
    :return: None
    """
    try:
        for __index in matrix:
            for j in __index:
                print(j)
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        matrix = []
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        for index in range(rows):
            matrix.append([])
            for _index in range(cols):
                matrix[index].append(int(input("Enter the value of {0} row and {1} column: ".format(index+1, _index+1))))
        print("The values of matrix given are: ")
        print_matrix(matrix)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
