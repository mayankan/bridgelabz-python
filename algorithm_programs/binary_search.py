def binary_word_search(filename):
    """Binary Search the word from word list
    Parameters:
        filename: text file
        word: input word to be searched in the file
    Returns:
        prints whether the word is found or not
    """
    my_list = []
    # Splitting the words and adding it to an empty list
    with open(filename, 'r') as f:
        for line in f:
            my_list.extend(line.lower().split())

    new_list = my_list
    # Taking input from the user
    word = input("Enter a word to be searched: ")
    # Traversing through the list to find the input word
    for i in range(len(new_list)):
        if word == new_list[i]:
            print("The word is found")
            break
    else:
        print("The word is not found")


def main():
    filename = "mytext.txt"
    binary_word_search(filename)


if __name__ == "__main__":
    main()
