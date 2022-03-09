def bubble_sort(array_input):
    """
    Sorting the elements using bubble sort.
    :param array_input: Input array provided by user for sorting.
    :return: sorted list.
    """
    try:
        print("Input array:", array_input)
        n = len(array_input)
        # Traverse through all the elements of array
        for i in range(n):
            for j in range(0, n - i - 1):
                # Swap if the element is greater than the next element
                if array_input[j] > array_input[j + 1]:
                    array_input[j], array_input[j + 1] = array_input[j + 1], array_input[j]
        return array_input
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        no_of_elements = int(input("Enter number of elements : "))
        array_input = []
        # Taking inputs from the user to fill up the values in the list
        for element in range(no_of_elements):
            _element = int(input("Enter a number: "))
            array_input.append(_element)
        sorted_array = bubble_sort(array_input)
        print("Sorted array: ")
        for index in sorted_array:
            print(index)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
