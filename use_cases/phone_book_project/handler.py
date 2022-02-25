# Import MyPhoneBook class from phone_book python module in order to call operations provided by the user.
from phone_book import MyPhoneBook


def welcome_screen():
    """
    Iterates welcome screen for the user to select operations in the Phone Book.
    """
    try:
        while True:
            print("Welcome to Your Phone Book.")
            print_stmts = ["Add Contact", "Modify Contact by Serial No.", "Delete Contact by Serial No.",
                           "See all Contacts", "Get Contact by Serial No.", "Show Sorted Contacts"]
            for print_stmt in range(len(print_stmts)):
                print("{} - {}".format(print_stmt+1, print_stmts[print_stmt]))
            # Asks user for input from the above options.
            operation_number = int(input("Enter the above number(1-6) to do the following operation: "))
            operations = MyPhoneBook()
            # Switcher dictionary used as switch case for the input operations to work.
            switcher = {
                1: operations.add_contact,
                2: operations.modify_contact,
                3: operations.delete_contact,
                4: operations.get_all_contacts,
                5: operations.get_contact,
                6: operations.sort_contacts
            }
            # Checks if input given by the user is between 1 and 6 else asks the input again.
            if 0 < operation_number <= 6:
                print(switcher.get(operation_number)())
            else:
                print("Invalid number entered. Please try again: ")
                continue
            # Checks if user wants to end the loop of performing operations in Phone Book.
            if input('Do you want to check your Phone Book again?(y/n): ') != 'y':
                break
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    try:
        welcome_screen()
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
