def get_prime_factors(input_no):
    prime_factors = []
    while input_no % 2 == 0:
        prime_factors.append(2)
        input_no = input_no / 2
    for index in range(3, int(input_no)+1, 2):
        while input_no % index == 0:
            prime_factors.append(index)
            input_no = input_no / index
    prime_factors.append(input_no) if input_no > 2 else pass
    return prime_factors


def main():
    input_no = int(input("Enter the number to find prime factors of: "))
    print(*get_prime_factors(input_no), sep="\n")


if __name__ == "__main__":
    main()
