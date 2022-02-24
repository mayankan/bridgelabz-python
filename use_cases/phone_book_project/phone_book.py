from contact import Contact
import file_management as fm


class MyPhoneBook:
    def __init__(self):
        self.data = fm.read_file()

    @staticmethod
    def to_dict(contact):
        return {"s_id": contact.s_id, "f_name": contact.f_name, "l_name": contact.l_name, "phone": contact.phone, "email": contact.email, "address": contact.address}

    @staticmethod
    def to_class(contact_dict):
        contact = Contact(contact_dict["s_id"], contact_dict["f_name"], contact_dict["l_name"], contact_dict["phone"], contact_dict["email"], contact_dict["address"])
        return contact

    def add_contact(self):
        s_id = fm.get_last_sid()
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        phone = int(input("Enter Phone Number: "))
        email = input("Enter Email Address: ")
        address = input("Enter Full Postal Address: ")
        contact = Contact(s_id, f_name, l_name, phone, email, address)
        contact_dict = self.to_dict(contact)
        fm.append_element(contact_dict)
        return "Added {} to Phone Book".format_map(contact.f_name)

    def get_all_contacts(self):
        all_contacts = fm.read_contacts()
        for contact in all_contacts:
            _contact = self.to_class(contact)
            print("Contact {}: Name: {} {}, Phone: {}, Email Id: {}, Address: {}".format(_contact.s_id, _contact.f_name, contact.l_name, contact.phone, _contact.email, _contact.address))
        return "Completed Printing All Contacts."


    def modify_contact(self):
        fm.modify_element_by_sid(s_no)
        fetch_contact = 'by s_no'
        print('if you want to edit email press 1')
        print('to exit enter n')
        return fetch_contact


    def delete_contact(self, s_no):
        fm.delete_element_by_sid(s_no)
        return contact


    def get_contact_by_id(self, search_by, value):
        s_no = search_by
        s_no_value = 1
        fetch_contact = 'contact fetched by s_no which is equal to 1'
        return fetch_contact


    def sort_contacts(self, short_key):
        value_of_short_key = short_key
        all_contacts = fm.read_file()
        return all_contacts


def main():
    try:
        MyPhoneBook()
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()