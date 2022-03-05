def factorial(number):
    if number == 1:
        return 1
    else:
        return number*factorial(number - 1)


def catalan_number(num):
    ct_num = (factorial(2*num))/((factorial(num+1))*factorial(num))
    return ct_num


def binary_tree():
    test_cases = int(input('Enter the number of test cases : '))
    case = []
    for i in range(0, test_cases):
        cases = int(input())
        cases = catalan_number(cases)
        case.append(cases)
    print([int(i) for i in case])


def main():
    binary_tree()


if __name__ == "__main__":
    main()
