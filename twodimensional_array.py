def print_matrix(matrix):
    """
    Prints 2 Dimensional Matrix values individually.
    :param matrix: list of list having 2 Dimensional matrix values
    :return: None
    """
    for i in matrix:
        for j in i:
            print(j)


def main():
    matrix = []
    rows = int(input("Enter number of rows:"))
    cols = int(input("Enter number of columns:"))
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(int(input("Enter the value of {0} row and {1} column".format(i+1, j+1))))
    print("The values of matrix given are: ")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
