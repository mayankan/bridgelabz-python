def check_triples(inputs_list):
    """
    Check Triplets in the list where the sum of three values equals to 0.
    :param inputs_list: input values to check triplets having a sum 0.
    :return: triplets in a list of list where the inner list contains the triplet values having sum 0.
    """
    triples = []
    for _index in range(2, len(inputs_list)):
        first_value = inputs_list[_index-2]
        second_value = inputs_list[_index-1]
        third_value = inputs_list[_index]
        if (first_value + second_value + third_value) == 0:
            triples.append([first_value, second_value, third_value])
    return triples


def main():
    inputs_list = []
    no_of_input = 0
    while no_of_input < 3:
        no_of_input = int(input("Enter number of integers you want to enter: "))
    print("Enter the values: ")
    for index in range(no_of_input):
        inputs_list.append(int(input()))
    triples = check_triples(inputs_list)
    if triples:
        print("Number of distinct Triplets are {} and Triplets are: ".format(len(triples)))
        print(*triples, sep=', ')
    else:
        print("There are no Triplets.")


if __name__ == "__main__":
    main()
