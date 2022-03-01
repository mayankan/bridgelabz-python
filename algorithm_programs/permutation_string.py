def permutation_string(_new_string):
    """Permutations of a string
    Parameters:
        _new_string: Takes a string as user input
    Returns:
        All the possible permutations of that string
    """
    if len(_new_string) == 1:
        return _new_string
    # Creating an empty list and appending the combinations of that string
    permutation_list = []
    for i in _new_string:
        remaining = [j for j in _new_string if j != i]
        a = permutation_string(remaining)

        for k in a:
            permutation_list.append(i + k)
    return permutation_list


def main():
    new_string = input("Enter a string: ")
    combinations = permutation_string(new_string)
    print(combinations)
    count = 0
    for characters in combinations:
        count += 1
    print("Number of Combinations: ", count)


if __name__ == "__main__":
    main()
