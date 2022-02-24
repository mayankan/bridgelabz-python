from phone_book import MyPhoneBook


def welcome_screen():
    try:
        while True:
            print("Welcome to Your Phone Book.")
            print("1 - Add Contact")
            print("2 - Modify Contact by Serial No.")
            print("3 - Delete Contact by Serial No.")
            print("4 - See all Contacts")
            print("5 - Get Contact by Serial No.")
            print("6 - Show Sorted Contacts")
            operation_number = int(input("Enter the above number(1-6) to do the following operation: "))
            operations = MyPhoneBook()
            switcher = {
                1: operations.add_contact,
                2: operations.modify_contact,
                3: operations.delete_contact,
                4: operations.get_all_contacts,
                5: operations.get_contact,
                6: operations.sort_contacts
            }
            if 0 < operation_number <= 6:
                print(switcher.get(operation_number)())
            else:
                print("Invalid number entered. Please try again: ")
                continue
            if input('Do you want to check your Phone Book again?(y/n): ') != 'y':
                break
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    welcome_screen()


if __name__ == "__main__":
    main()
