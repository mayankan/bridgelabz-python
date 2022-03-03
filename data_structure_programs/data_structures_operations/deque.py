class Deque:
    """This class stores the characters of the string and performs various methods
    """

    def __init__(self):
        self.deque = []

    def add_front(self, item):
        """This function adds the item to the left of the deque
        Parameters:
            item: The value to be added to the deque
        Returns a modified deque
        """
        self.deque.insert(0, item)

    def add_rear(self, item):
        """This function adds an item to the right of the deque
        Parameters:
              item: The value to be added
        Returns a modified deque
        """
        self.deque.append(item)

    def remove_front(self):
        """This function removes an item from the left of the deque
        Returns:
              The deleted value
        """
        return self.deque.pop(0)

    def remove_rear(self):
        """This function removes an item from the right side of the deque
        Returns:
              The removed value
        """
        return self.deque.pop()

    def is_empty(self):
        """This method checks whether the deque is empty or not
        """
        return self.deque == []

    def get_size(self):
        """This method returns the number of items in the deque
        """
        return len(self.deque)

    def get_deque(self):
        """This method prints the items of the deque
        """
        for item in self.deque:
            print(item, )

    def palindrome_checker(self, input_string):
        """This function is a check on a string for palindrome
        Parameters:
              input_string: The string as user input
        Returns:
              True if Palindrome and False if not
        """
        input_string = input_string.lower()
        for character in input_string:
            self.add_rear(character)

        if self.deque == self.deque[::-1]:  # Comparing the list with its reversed list
            print("{} is a Palindrome".format(input_string))
        else:
            print("{} is not a Palindrome".format(input_string))
