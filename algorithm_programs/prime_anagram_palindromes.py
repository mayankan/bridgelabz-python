def palindrome_prime(lower, upper):
    """Palindrome Prime numbers in a given range
    Parameters:
        lower: lower value of that range
        upper: upper value of the range
    Returns:
        A list of prime numbers that are also palindrome in that range
    """

    def palindrome(num):
        """Creating a function to check if the number is palindrome or not
        Parameters:
            num: integer value
        Returns:
            num if it is palindrome
        """
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

    print("Palindrome Prime numbers between ", lower, " and ", upper, " are: ")
    my_list = []
    # Traversing through the range
    for num in range(lower, upper + 1):
        if num > 1:
            # Check for prime numbers
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                # Check whether the prime number is palindrome and then adding it to the list
                my_list.append(palindrome(num))
    print(my_list)


def main():
    lower = int(input("Enter a lower limit: "))
    upper = int(input("Enter an upper limit: "))

    palindrome_prime(lower, upper)


if __name__ == "__main__":
    main()
