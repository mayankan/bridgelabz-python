import json
import os
import contact


class FileManagement:
    def __init__(self):
        self.data = {}
        self.file_name = "address_book.json"
        self.create_new_book(self.file_name)

    def create_new_book(self):
        self.data = {'contacts': []}
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as phone_book:
                json.dump(self.data, phone_book, indent=4)
                phone_book.close()
        else:
            with open(self.file_name, 'r') as phone_book:
                self.data = json.load(phone_book)

    def open_file(self, file_name):
        """This method opens an existing json file.
        :return: Data fetched from Json File
        """
        try:
            with open(file_name, 'r') as phone_book:
                self.data = json.load(phone_book)
        except FileNotFoundError:
            self.create_new_book(self.file_name)
        except Exception as e:
            print("{} is raised.".format(str(e)))

    def create_contact_to_book(self, new_contact):
        with open("address_book.json", 'a') as phone_book:
            json.dump(self.file_name, phone_book)
        return new_contact

    def update_contact_by_id(contact_id):
        with open("address_book.json", 'w') as phone_book:
            json.dump()

    def delete_contact_by_id(contact_id):
        with open("address_book.json", 'w') as phone_book:
            json.dump()



