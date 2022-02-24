from phone_book import MyPhoneBook


def welcome_screen():
    try:
        while True:
            print("Welcome to Your Address Book.")
            print("1 - Add Contact")
            print("2 - Modify Contact by Id")
            print("3 - Delete Contact by Id")
            print("4 - See all Contacts")
            print("5 - Get Contact by Id")
            print("6 - Show Sorted Contacts")
            print("Enter the above number(1-6) to do the following operation.")
            operation_number = int(input())
            switcher = {
                1: MyPhoneBook.add_contact(),
                2: MyPhoneBook.modify_contact(),
                3: MyPhoneBook.delete_contact(),
                4: MyPhoneBook.get_all_contacts(),
                5: MyPhoneBook.get_contact_by_id(),
                6: MyPhoneBook.sort_contacts()
            }
            if 0 < operation_number <= 6:
                print(switcher.get(operation_number))
            else:
                print("Invalid number entered. Please try again: ")
                continue
            if input('Do you want to check your Address Book again?(y/n): ') != 'y':
                break
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    welcome_screen()


if __name__ == "__main__":
    main()
