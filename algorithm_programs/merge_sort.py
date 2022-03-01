def merge_sort(elements_number):
    """Merge Sort
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

    def small_sort(array_input):
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


def main():
    elements_number = int(input("Enter number of elements : "))
    merge_sort(elements_number)


if __name__ == "__main__":
    main()
