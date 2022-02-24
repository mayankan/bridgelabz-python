# Importing Packages to do Operations
from contact import Contact
import file_management as fm


# MyPhoneBook class consists of all the logics and operations performed in order to give user a Phone Book experience.
class MyPhoneBook:
    def __init__(self):
        try:
            fm.read_create_new_book()
        except Exception as e:
            print("{} is raised.".format(str(e)))

    @staticmethod
    def to_dict(contact):
        """
        Converts Contact class instance values to a dictionary format.
        :param contact: Contact class instance holding contact values.
        :return:
        """
        try:
            return {"s_id": contact.s_id, "f_name": contact.f_name, "l_name": contact.l_name, "phone": contact.phone,
                    "email": contact.email, "address": contact.address}
        except Exception as e:
            print("{} is raised.".format(str(e)))

    @staticmethod
    def to_class(contact_dict):
        """
        Converts Dictionary of contact values to Contact class values and returns it.
        :param contact_dict: Dictionary of contact values.
        :return:
        """
        try:
            contact = Contact(contact_dict["s_id"], contact_dict["f_name"], contact_dict["l_name"], contact_dict["phone"],
                              contact_dict["email"], contact_dict["address"])
            return contact
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def add_contact(self):
        """
        Adds Contact to Phone Book and returns the First name of contact added.
        :return: First name of contact added.
        """
        try:
            s_id = fm.get_last_sid()
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            phone = int(input("Enter Phone Number: "))
            email = input("Enter Email Address: ")
            address = input("Enter Full Postal Address: ")
            contact = Contact(s_id + 1, f_name, l_name, phone, email, address)
            contact_dict = self.to_dict(contact)
            fm.append_element(contact_dict)
            return "Added {} to Phone Book".format(contact.f_name)
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def get_all_contacts(self):
        """
        Prints all contacts in the Phone Book and returns the message of completion after printing.
        :return: A message stating completion of printing all contacts in the phone book.
        """
        try:
            all_contacts = fm.read_contacts()
            for contact in all_contacts:
                _contact = self.to_class(contact)
                print("Contact {0}: Name: {1} {2}, Phone: {3}"
                      ", Email Id: {4}, Address: {5}".format(_contact.s_id + 1, _contact.f_name, _contact.l_name,
                                                             _contact.phone, _contact.email, _contact.address))
            return "Completed Printing All Contacts."
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def get_contact(self):
        """
        Returns Contact at serial number given by the user.
        :return: Contact details of user at the specified serial number.
        """
        try:
            s_no = int(input("Enter Serial No. to Get Contact details: "))
            contact = fm.get_element_by_sid(s_no - 1)
            _contact = self.to_class(contact)
            return "Contact fetched by Serial {}: Name: {} {}, Phone: {}" \
                   ", Email Id: {}, Address: {}".format(s_no, _contact.f_name, _contact.l_name, _contact.phone,
                                                        _contact.email, _contact.address)
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def modify_contact(self):
        """
        Modifies Contact at serial number given by the user.
        :return: Contact details of user at the specified serial number if they exist.
        """
        try:
            s_no = int(input("Enter Serial No. to Modify Contact details: "))
            contact = fm.get_element_by_sid(s_no - 1)
            if contact:
                contact = self.to_class(contact)
                f_name = input("Enter First Name ({}): ".format(contact.f_name))
                if f_name == "":
                    f_name = contact.f_name
                l_name = input("Enter Last Name ({}): ".format(contact.l_name))
                if l_name == "":
                    l_name = contact.l_name
                phone = input("Enter Phone Number ({}): ".format(contact.phone))
                while type(phone) != int and phone == "":
                    phone = contact.phone if phone == "" else input("Enter Phone Number correctly ({}): "
                                                                    .format(contact.phone))
                email = input("Enter Email Address ({}): ".format(contact.email))
                if email == "":
                    email = contact.email
                address = input("Enter Full Postal Address ({}): ".format(contact.address))
                if address == "":
                    address = contact.address
                _contact = Contact(s_no - 1, f_name, l_name, phone, email, address)
                contact_dict = self.to_dict(_contact)
                fm.modify_element_by_sid(contact_dict)
                return "Contact updated by Serial {}: Name: {} {}, Phone: {}" \
                       ", Email Id: {}, Address: {}".format(s_no, _contact.f_name, _contact.l_name, _contact.phone,
                                                            _contact.email, _contact.address)
            else:
                return "No Contact found for Serial {}.".format(s_no)
        except Exception as e:
            print("{} is raised.".format(str(e)))

    @staticmethod
    def delete_contact():
        """
        Returns True after deleting the contact at serial number provided by the user else False.
        :return: True or False if Contact is deleted or not.
        """
        try:
            s_no = int(input("Enter Serial No. to Delete Contact details: "))
            deleted = fm.delete_element_by_sid(s_no - 1)
            return "Contact with Serial {} deleted successfully.".format(s_no) if deleted else "No Contact found for " \
                                                                                               "Serial {}.".format(s_no)
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def sort_contacts(self):
        """
        Prints all contacts in the Phone Book after sorting and returns the message of completion after printing.
        :return: A message stating completion of printing all sorted contacts in the phone book.
        """
        try:
            print("Inside Sort Contact")
            while True:
                column = int(input("Enter Column no. to sort Contacts by the specified column.\n"
                                   "1 - First Name, 2 - Last Name, 3 - Phone Number, \n"
                                   "4 - Email Address, 5 - Full Postal Address: "))
                derive_column = {
                    1: "f_name",
                    2: "l_name",
                    3: "phone",
                    4: "email",
                    5: "address",
                }
                if 0 < column <= 5:
                    sorted_contacts = fm.sort_elements_by_key(derive_column.get(column))
                    for contact in sorted_contacts:
                        _contact = self.to_class(contact)
                        print("Contact {}: Name: {} {}, Phone: {}" \
                              ", Email Id: {}, Address: {}".format(_contact.s_id + 1, _contact.f_name, _contact.l_name,
                                                                   _contact.phone, _contact.email, _contact.address))
                    break
                else:
                    print("Invalid number entered. Please try again: ")
                    continue
            return "Completed Printing Sorted Contacts."
        except Exception as e:
            print("{} is raised.".format(str(e)))


def main():
    try:
        print("Inside Phone Book Main")
        phone_book = MyPhoneBook()
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
