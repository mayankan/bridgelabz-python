import random


def generate_random_values(no_of_times):
    """
    Generates random values between 0 and 1 given number of times and gives percentage of getting 1 in the all values generated.
    :param no_of_times: number of times random value is to be generated.
    :return: percentage of 1 in all values generated randomly.
    """
    random_flips = []
    for index in range(no_of_times):
        flip_coin = random.random()
        random_flips.append(1) if flip_coin >= 0.5 else random_flips.append(0)
    result = (sum(random_flips)/no_of_times)
    return result


def main():
    no_of_times = 0
    while no_of_times < 1:
        no_of_times = int(input("Enter the number of times to Flip Coin: "))
    print(generate_random_values(no_of_times))


if __name__ == "__main__":
    main()
