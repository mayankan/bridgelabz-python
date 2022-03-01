def insertion_sort(elements_number):
    """Insertion Sort
    Parameters:
        elements_number: the length of array as input
    Returns:
        Sorted array
    """
    array_input = []
    # Taking inputs from the user to fill up the values in the list
    for i in range(0, elements_number):
        ele = int(input("Enter a number: "))
        array_input.append(ele)

    print("Input array:", array_input)
    # Traversing from 1 to length of the array
    for i in range(1, len(array_input)):
        k = array_input[i]
        # Move elements of array that are greater than k to one position ahead of their current
        j = i - 1
        while j >= 0 and k < array_input[j]:
            array_input[j + 1] = array_input[j]
            j -= 1
        array_input[j + 1] = k

    print("Sorted array: ")
    for i in range(len(array_input)):
        print(array_input[i])


def main():
    elements_number = int(input("Enter number of elements : "))
    insertion_sort(elements_number)


if __name__ == "__main__":
    main()
