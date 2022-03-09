def insertion_sort(array_input):
    """
    Sorting the elements using insertion sort.
    :param array_input: Input array provided by user for sorting.
    :return: sorted list.
    """
    try:
        print("Input array:", array_input)
        # Traversing from 1 to length of the array
        for element in range(1, len(array_input)):
            cur_pos = array_input[element]
            # Move elements of array that are greater than k to one position ahead of their current
            next_pos = cur_pos - 1
            while next_pos >= 0 and cur_pos < array_input[next_pos]:
                array_input[next_pos + 1] = array_input[next_pos]
                next_pos -= 1
            array_input[next_pos + 1] = cur_pos
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
        sorted_array = insertion_sort(array_input)
        print("Sorted array: ")
        for index in sorted_array:
            print(index)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
