from data_structure_programs.data_structures_operations.stack import Stack


def main():
    expression = input("Enter the expression: ")

    expression_object = Stack()
    result = expression_object.paren_balance(expression)
    print(result)


if __name__ == "__main__":
    main()

