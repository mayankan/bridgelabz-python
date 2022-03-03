from data_structure_programs.data_structures_operations.linked_list import LinkedList


def main():
    linked_list = LinkedList()
    # Getting the number from the file
    file_name = input("\nEnter the File Name: ")
    file_hand = open(file_name, 'r')
    file_lines = file_hand.readlines()
    for line in file_lines:
        numbers = line.split()
        for number in numbers:
            linked_list.insert_at_end(int(number))
    print("\nLinked List before sorting:")
    linked_list.traverse_list()

    linked_list.bubble_sort()
    print("\nLinked List after sorting")
    linked_list.traverse_list()

    # Searching the number in the linked list
    search_number = int(input("\nEnter the number to be searched : "))
    if linked_list.search_item(search_number):
        linked_list.delete_element(search_number)
        print(search_number, " found in the Linked List and deleted")
        linked_list.traverse_list()
    else:
        print(search_number, " not found in the Linked List and hence added to the list")
        linked_list.insert_at_end(search_number)
        linked_list.bubble_sort()
        linked_list.traverse_list()


if __name__ == "__main__":
    main()
