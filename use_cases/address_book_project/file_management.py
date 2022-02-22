import json
import os
import contact


def create_new_book():
    file_name = 'address_book.json'  # input from user
    if os.path.exists(file_name):
        pass
    else:
        with open(file_name, 'w') as phone_book:
            json.dump([], phone_book)


def add_data_to_book(new_contact):
    with open("address_book.json", 'a') as phone_book:
        json.dump(new_contact, phone_book)
    return new_contact


def delete(contact_id):
    with open("address_book.json", 'w') as phone_book:
        json.dump()


def read_file(file_name):
    reading_file = 'logic'
    return 'file data'


def open_file(file_name):
    pass

