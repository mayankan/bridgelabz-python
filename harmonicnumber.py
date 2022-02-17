def calc_harmonic_sum(harmonic_limit):
    harmonic_sum = 0
    for index in range(1, harmonic_limit+1):
        harmonic_sum = harmonic_sum + 1 / index
    return harmonic_sum


def main():
    harmonic_limit = 0
    while harmonic_limit == 0:
        harmonic_limit = int(input("Enter the number till which you want to print harmonic number: "))
    print(calc_harmonic_sum(harmonic_limit))


if __name__ == "__main__":
    main()
