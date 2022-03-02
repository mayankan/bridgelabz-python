def merge_sort(array):
    if len(array) > 1:

        #  middle_index is the point where the array is divided into two sub-arrays
        middle_index = len(array) // 2
        left_array = array[:middle_index]
        right_array = array[middle_index:]

        # Sort the two halves
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0

        # Until we reach either end of either left_array or right_array, pick larger among
        # elements left_array and right_array and place them in the correct position at A[p..r]
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        print(left_array, right_array)

        # When we run out of elements in either left_array or right_array,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        print(left_array)

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
        print(right_array)


# Print the array
def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


def main():
    array = [6, 5, 12, 10, 9, 1]
    merge_sort(array)
    print("Sorted array is: ")
    print_list(array)


# Driver program
if __name__ == '__main__':
    main()
