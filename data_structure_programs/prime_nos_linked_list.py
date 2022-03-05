import data_structures_operations.stack as stack
import prime_nos_queue


def linked_list_operation(input_list):
    stacked_list = stack.Stack()
    for i in input_list:
        stacked_list.push(i)
    return stacked_list


def linked_list_removal(input_list):
    no_of_elements = int(input("Enter the number of elements that you want to remove : "))
    for index in range(no_of_elements):
        input_list.pop()
    return input_list


def main():
    # program to print prime numbers from 0 to 1000
    prime_nos = prime_nos_queue.print_prime()
    # checking whether the number is anagram or not
    prime_anagrams = prime_nos_queue.check_anagrams(prime_nos)
    list_anagrams = prime_nos_queue.anagram_and_dictform(prime_anagrams)
    linked_list = linked_list_operation(list_anagrams)
    linked_list.display()
    print("\n")
    de_stacked_list = linked_list_removal(linked_list)
    print("\n De-stacked list is : ")
    de_stacked_list.display()
    print("\n")


if __name__ == "__main__":
    main()
