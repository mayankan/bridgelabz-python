import re
import datetime


def regex_string(input_string):
    """
    uses regex to replace custom message in given input string.
    :param input_string: given input string to be replaced by regex.
    :return: modified string as per problem statement.
    """
    try:
        first_name = input("Enter first name: ")
        full_name = (input("Enter full name: "))
        mobile_number = input("Enter mobile number: ")
        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        # Converting the year, month, day into a date format
        date_format = datetime.date(year, month, day)
        date = str(date_format)
        # Replacing the necessary values using sub function from the re module
        modified_message = re.sub("<<name>>", first_name, message_string)
        modified_message = re.sub("<<full name>>", full_name, modified_message)
        modified_message = re.sub("xxxxxxxxxx", mobile_number, modified_message)
        modified_message = re.sub("01/01/2016", date, modified_message)
        return modified_message
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        message_string = "Hello <<name>>, We have your full name as <<full name>> in our system. \n" \
                         "Your contact number is 91-xxxxxxxxxx. \n" \
                         "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
        print(regex_string(message_string))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
