class Queue:
    """This class stores items in a First In First Out manner.
    the following class creates and empty queue and performs the following methods
    """

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """This method adds an item to the end of the queue
        Parameters:
            item: The value to be added to the queue
        """
        self.items.append(item)

    def dequeue(self):
        """This method removes the item at the beginning of the queue
        Returns:
            The item that is removed
        """
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def is_empty(self):
        """This method checks whether the queue is empty or not
        """
        return self.items == []

    def get_size(self):
        """This method returns the number of items in the queue
        """
        return len(self.items)

    def get_queue(self):
        """This method prints the items in the queue
        """
        for item in self.items:
            print(item, )

    def cash_counter(self):
        """This is a function where people come to deposit cash or withdraw cash
        Input: Asking individuals to deposit or withdraw the amount
        """

        cash = 10000  # Initiating a variable which consists of the amount the bank has
        deposit = 0
        withdraw = 0

        while True:
            print("1 --> Deposit Cash")
            print("2 --> Withdraw Cash")
            print("3 --> Exit")
            # Taking user inputs for the type of transaction
            choice = int(input("Please enter a value: "))
            # If the user wants to deposit the cash
            if choice == 1:
                self.enqueue(1)
                # Amount to be deposited
                amount = int(input("Enter the amount to be desposited: "))
                if amount == 0:
                    print("Enter Amount!")
                else:
                    deposit += amount
                    cash += amount  # Adding the deposit to the total cash
                    print("Thank You!\nCash Deposited Successfully\n")
                self.dequeue()
            # If the user wants to withdraw cash
            elif choice == 2:
                withdraw += 1
                self.enqueue(1)

                amount = int(input("Enter the amount to withdraw: "))

                if cash >= amount:  # Checking if the amount to be withdrawed is available or not
                    deposit -= amount
                    cash -= amount  # Subtracting the withdrawal amount from the total cash
                    print("Thank You!\nCash Withdrawal Successful\n")
                else:
                    # If the withdrawal amount is more than the cash available
                    print("Insufficient Balance!\n")
                    self.dequeue()
            # If the user wants to exit
            elif choice == 3:
                quit()

            else:
                self.cash_counter()