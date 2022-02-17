def pow_of_2(multiple_limit):
    output_list = []
    for index in range(1, multiple_limit+1):
        output_list.append(2 ** index)
    return output_list


def main():
    multiple_limit = 35
    while multiple_limit >= 31 or multiple_limit < 0:
        multiple_limit = int(input("Enter the root of number till which you want to print multiples of 2: "))
    print(*pow_of_2(multiple_limit), sep="\n")


if __name__ == "__main__":
    main()
