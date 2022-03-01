def bubble_sort(elements_number):
    """Bubble Sort
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

    n = len(array_input)
    # Traverse through all the elements of array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if array_input[j] > array_input[j + 1]:
                array_input[j], array_input[j + 1] = array_input[j + 1], array_input[j]

    print("Sorted array: ")
    for i in range(len(array_input)):
        print(array_input[i])


def main():
    elements_number = int(input("Enter number of elements : "))
    bubble_sort(elements_number)


if __name__ == "__main__":
    main()
