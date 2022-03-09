def permutation_string(_input_string):
    """
    Returns the permutation of given input string by the user.
    :param _input_string: input string given by the user.
    :return: permutations of all the characters in the string.
    """
    try:
        if len(_input_string) == 1:
            return _new_string
        # Creating an empty list and appending all the combinations of that string
        permutation_list = []
        for char in _input_string:
            remaining_chars = [ch for ch in _input_string if ch != i]
            recursive_fn = permutation_string(remaining_chars)
            for each_char in recursive_fn:
                permutation_list.append(char + each_char)
        return permutation_list
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        input_string = input("Enter a string: ")
        combinations = permutation_string(input_string)
        print(combinations)
        print("Number of Combinations: ", len(combinations))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
