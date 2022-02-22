def welcome_screen():
    try:
        while True:
            print("Welcome to Your Address Book.")
            print("1 - Add Contact")
            print("2 - Modify Contact by Id")
            print("3 - Delete Contact by Id")
            print("4 - See all Contacts")
            print("5 - Get contact by Id")
            print("Enter the above number(1-5) to do the following operation.")
            operation_number = int(input())
            if input('Do you want to check your Address Book again?(y/n): ') != 'y':
                break
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    welcome_screen()


if __name__ == "__main__":
    main()
