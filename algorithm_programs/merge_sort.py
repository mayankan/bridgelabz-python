def merge_sort(array_input):
    """
    Sorting the elements using merge sort.
    :param array_input: Input array provided by user for sorting.
    :return: sorted list.
    """
    print("Input array:", array_input)
    # Dividing the array into two halves until length of array is 1
    if len(array_input) > 1:
        mid = len(array_input) // 2
        L = array_input[:mid]
        R = array_input[mid:]

        small_sort(L)  # Sorting the first half
        small_sort(R)  # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array_input[k] = L[i]
                i += 1
            else:
                array_input[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array_input[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array_input[k] = R[j]
            j += 1
            k += 1
    return array_input


def main():
    no_of_elements = int(input("Enter number of elements : "))
    array_input = []
    # Taking inputs from the user to fill up the values in the list
    for element in range(no_of_elements):
        _element = int(input("Enter a number: "))
        array_input.append(_element)
    sorted_array = merge_sort(array_input)
    print("Sorted array: ")
    for index in sorted_array:
        print(index)


if __name__ == "__main__":
    main()
