from data_structure_programs.data_structures_operations.deque import Deque


def main():
    input_string = input("Enter the string to be checked: ")

    deque_object = Deque()
    deque_object.palindrome_checker(input_string)


if __name__ == "__main__":
    main()
