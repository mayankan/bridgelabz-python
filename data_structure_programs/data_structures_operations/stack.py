class Stack:
    """The following class creates an empty stack and performs various methods mentioned below
    """

    def __init__(self):
        self.items = []

    def push(self, element):
        """It adds the item to the top of the stack
        Parameters:
            element: The value to be added to the stack
        """
        self.items.append(element)

    def pop(self):
        """This function removes the top item from the stack and the stack is modified
        It needs no parameters
        Returns:
            The item that is removed
        """
        return self.items.pop()

    def is_empty(self):
        """This function checks whether the stack is empty or not
        Returns True if empty or else False
        """
        return self.items == []

    def top(self):
        """This function returns the top item of the stack
        """
        return self.items[-1]

    def get_stack(self):
        """This fun function returns all the items of the stack
        """
        return self.items

    def get_size(self):
        """This function returns the number of items in the stack
        """
        return len(self.items)

    def paren_balance(self, expression):
        """This function takes an arithmetic expression  and checks whether the expression is balanced or not using stack
        Parameters:
            expression: an arithmetic expression taken from an user input
        Returns:
            Check Whether the expression is balanced or not
        """

        open_paren = "({["  # A variable containing only the open parenthesis
        closed_paren = ")}]"  # A variable containing only the closed parenthesis

        for bracket in expression:
            if bracket in open_paren:  # Pushing the bracket if it is a Open parenthesis
                self.push(bracket)
            elif bracket in closed_paren:
                if self.is_empty():  # Checking if the stack is empty
                    balanced = False
                    break
                self.pop()  # Removing the bracket if it is a Closed parenthesis
        else:
            if self.is_empty():  # Returning True if stack is empty i.e. balanced
                balanced = True
            else:
                balanced = False  # Returning False if the stack is not empty i.e. unbalanced
        if balanced:
            print("Expression '", expression, "' is Balanced")
        else:
            print("Expression '", expression, "' is not Balanced")