from data_structure_programs.data_structures_operations.linked_list import LinkedList


def main():
    linked_list = LinkedList()
    # Getting the words from the file
    file_name = input("\nEnter the File Name: ")
    file_hand = open(file_name, 'r')
    file_lines = file_hand.readlines()
    for line in file_lines:
        words = line.lower().split()
        for word in words:
            linked_list.insert_at_end(word)
    print("\n File contents in the List are:")
    linked_list.traverse_list()

    # Searching the word in the Linked List
    search_word = input("\nEnter the word to be searched : ")
    if linked_list.search_item(search_word):
        linked_list.delete_element(search_word)
        print("Word", search_word, " found in the Linked List and deleted")
    else:
        print("Word", search_word, " not found in the Linked List")

    # Updated Linked list is stored in the file words_output.txt
    file_name = "words_output.txt"
    file_hand = open(file_name, 'w+')
    a = linked_list.f_display()
    # print(a)
    file_hand.write(a)
    file_hand.close()
    print("File created with filename words_output.txt")


if __name__ == "__main__":
    main()
