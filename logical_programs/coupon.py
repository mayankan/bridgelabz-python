import random


def coupon_numbers(no_of_coupons):
    """Coupon Numbers
    Parameters:
        no_of_coupons: number of distinct coupon numbers
    Returns:
        total random numbers needed to print all the distinct numbers
    """
    my_list = []
    count = 0
    while len(my_list) < no_of_coupons:
        x = random.randint(1, no_of_coupons)
        count += 1
        # Checking if the random number is a new number
        if x not in my_list:
            my_list.append(x)
    return "Total random numbers needed to have all distinct numbers: ", count


def main():
    try:
        distinct = int(input("Enter number of distinct coupon number: "))
        if distinct > 0:
            random_coupon_count = coupon_numbers(distinct)
            print(random_coupon_count)
        else:
            print("Enter a positive value!")
    except Exception as e:
        if e == ValueError:
            print("Enter an integer value!")


if __name__ == "__main__":
    main()
