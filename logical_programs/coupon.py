import random


def coupon_numbers(no_of_coupons):
    """
    Returns number of Random numbers to have all distinct coupon numbers.
    :param no_of_coupons: Number of coupons entered by the user to have random number of coupons.
    :return: count of total random numbers to have all distinct numbers.
    """
    try:
        coupon_nos = []
        count = 0
        while len(coupon_nos) < no_of_coupons:
            x = random.randint(1, no_of_coupons)
            count += 1
            # Checking if the random number is a new number
            if x not in coupon_nos:
                coupon_nos.append(x)
        return count
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        distinct = int(input("Enter number of distinct coupon number: "))
        if distinct > 0:
            random_coupon_count = coupon_numbers(distinct)
            print("Total random numbers needed to have all distinct numbers: ", random_coupon_count)
        else:
            print("Enter a positive value!")
    except Exception as e:
        if e == ValueError:
            print("Enter an integer value!")
        else:
            print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
