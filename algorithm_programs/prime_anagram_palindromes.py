def palindrome_prime(lower, upper):
    """
    Prime Palindrome numbers in a given range - lower to upper.
    :param lower: lower value of given range
    :param upper: upper value of given range
    :return: A list of prime palindrome numbers in given range
    """
    try:
        prime_palindromes = []
        # Traversing through the range
        for num in range(lower, upper + 1):
            if num > 1:
                # Check for prime numbers
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    # Check whether the prime number is palindrome and then adding it to the list
                    prime_palindromes.append(palindrome(num))
        return prime_palindromes
    except Exception as e:
        print("{} is raised".format(e))


def palindrome(num):
    """
    Returns number if it is Palindrome
    :param num: given number to check if it is palindrome.
    :return: number if it is palindrome else None.
    """
    try:
        rem = 0
        rev = 0
        n = int(num)
        if n > 9:
            while n > 0:
                rem = n % 10
                n = int(n / 10)
                rev = rev * 10 + rem
                if rev == num:
                    print(num)
                else:
                    continue
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        lower = int(input("Enter a lower limit: "))
        upper = int(input("Enter an upper limit: "))
        print(palindrome_prime(0, 1000))
        # print(palindrome_prime(lower, upper))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
