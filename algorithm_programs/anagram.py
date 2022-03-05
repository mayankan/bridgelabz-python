def check(s1, s2):
    """
    Checks if both given strings are anagrams or not.
    :param s1: first string given by the user.
    :param s2: second string given by the user.
    :return: True if strings are anagrams else false.
    """
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


def main():
    string_1 = input("Enter first string: ")
    string_2 = input("Enter first string: ")
    print("Both the strings are anagrams") if check(string_1, string_2) else print("Both the strings are not anagrams.")


if __name__ == "__main__":
    main()
