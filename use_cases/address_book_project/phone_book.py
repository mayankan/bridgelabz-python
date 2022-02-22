from contact import Person
import file_management
import contact


class My_Phone_Book:
    def __init__(self, file_name):
        self.file = file_name

    def get_all_contacts(self):
        all_contacts = read_file()
        return all_contacts

    def add_contact(self):
        contact = Person()
        contact_json = 'contact'
        return

    def delete_contact(self, s_no):
        contact = 'deleted contact'
        return contact

    def modify_contact(self, s_no):
        fetch_contact = 'by s_no'
        print('if you want to edit email press 1')
        print('to exit enter n')
        return fetch_contact

    def search(self, search_by, value):
        s_no = search_by
        s_no_value = 1
        fetch_contact = 'contact fetched by s_no which is equal to 1'
        return fetch_contact

    def arrange_contact(self, short_key):
        value_of_short_key = short_key
        all_contacts = self.get_all_contacts()
        return all_contacts