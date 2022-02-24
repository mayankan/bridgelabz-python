# Import Packages
import json # For Json load and dump
import os # Checking json file present or not


def read_file():
    """
    Reads Phone Book Json File.
    :return: All the contacts available in Phone Book Json File.
    """
    try:
        with open("phone_book.json", 'r') as phone_book:
            read_data = json.load(phone_book)
        return read_data
    except Exception as e:
        print("{} is raised.".format(str(e)))


def read_contacts():
    """
    Reads Contacts key from Initial Dictionary in Phone Book Json File.
    :return: List of Contacts containing multiple dictionaries of Contacts.
    """
    try:
        data = read_file()
        fetched_contacts = list(data['contacts'])
        return fetched_contacts
    except Exception as e:
        print("{} is raised.".format(str(e)))


def write_file(data):
    """
    Writes data to Phone Book Json File.
    :param data: Data to be written in Phone Book Json File.
    :return:
    """
    try:
        with open("phone_book.json", 'w') as phone_book:
            json.dump(data, phone_book)
            phone_book.close()
    except Exception as e:
        print("{} is raised.".format(str(e)))


def write_contacts(data):
    """
    Writes data to contacts key in the Phone Book Json File.
    :param data: List of dictionaries of contacts to be written in Phone Book Json File.
    :return:
    """
    try:
        updated_data = {'contacts': data}
        write_file(updated_data)
    except Exception as e:
        print("{} is raised.".format(str(e)))


def read_create_new_book():
    """
    Checks whether Phone Book Json File is there and creates it if it is not there.
    :return: New Contacts Data from Phone Book Json File.
    """
    try:
        data = {'contacts': []}
        if not os.path.exists("phone_book.json"):
            write_file(data)
        else:
            read_data = read_file()
            if read_data == None:
                write_file(data)
            else:
                data = read_data
        return data
    except Exception as e:
        print("{} is raised.".format(str(e)))


def append_element(contact):
    """
    Adds an element at the end of Phone Book List.
    :param contact: Element to be added at the end of Phone Book List.
    :return:
    """
    try:
        data = read_contacts()
        data.append(contact)
        write_contacts(data)
    except Exception as e:
        print("{} is raised.".format(str(e)))


def get_element_by_sid(s_id):
    """
    Returns Element by s_id in the List of Elements of Phone Book Json File.
    :param s_id: Serial Id to Fetch the element in the Phone Book Json File.
    :return: Element specific to s_id unique value or None if No Element corresponds to the s_id.
    """
    try:
        data = read_contacts()
        read_element = next((item for item in data if item["s_id"] == s_id), None)
        return read_element
    except Exception as e:
        print("{} is raised.".format(str(e)))


def get_last_sid():
    """
    Returns Last Element s_id in the List of Elements of Phone Book Json File.
    :return: Last Element s_id in the List of Elements of Phone Book Json File.
    """
    try:
        data = read_contacts()
        if len(data) > 0:
            read_element = data[len(data) - 1]
            return read_element["s_id"]
        else:
            return -1
    except Exception as e:
        print("{} is raised.".format(str(e)))


def modify_element_by_sid(contact):
    """
    Updates the values of element by s_id in the List of Elements of Phone Book Json File.
    :param contact: Serial Id to Update the element in the Phone Book Json File.
    :return: Element updated to s_id unique value or None if No Element corresponds to the s_id.
    """
    try:
        data = read_contacts()
        read_index = next((i for i, item in enumerate(data) if item["s_id"] == contact["s_id"]), None)
        if read_index:
            data[read_index] = contact
            write_contacts(data)
            return contact
        else:
            return None
    except Exception as e:
        print("{} is raised.".format(str(e)))


def delete_element_by_sid(s_id):
    """
    Deletes the values of element by s_id in the List of Elements of Phone Book Json File.
    :param s_id: Serial No to Delete the element in the Phone Book Json File.
    :return: True if Element is deleted else False if No Element corresponds to the s_id.
    """
    try:
        data = read_contacts()
        read_index = next((i for i, item in enumerate(data) if item["s_id"] == s_id), None)
        if read_index:
            del data[read_index]
            write_contacts(data)
            return True
        else:
            return False
    except Exception as e:
        print("{} is raised.".format(str(e)))


def sort_elements_by_key(key):
    """
    Sorts List of Elements from Initial Dictionary in Phone Book Json File.
    :param key: key column by which list of elements are sorted.
    :return: List of Elements sorted by key.
    """
    try:
        data = read_contacts()
        data = sorted(data, key=lambda i: i[key])
        return data
    except Exception as e:
        print("{} is raised.".format(str(e)))


def main():
    try:
        read_create_new_book()
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
