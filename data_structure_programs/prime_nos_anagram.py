import prime_nos_queue


def prime_and_anagram_printing(prime_list, anagram_list):
    i = 0
    new_array_anagram = []
    new_array_prime = []
    for j in range(0, 1000, 100):

        new_array_p = []
        new_array_a = []

        for q in prime_list:
            if q in range(j, j + 100):
                new_array_p.append(q)

        for a in anagram_list:
            if a in range(j, j + 100):
                new_array_a.append(a)

        new_array_anagram.append(new_array_a)
        new_array_prime.append(new_array_p)

        print("\n")
        print("The prime numbers in the range {} to {} is :".format(j, j + 100))
        print(new_array_prime[i])
        print("\r")
        print("The anagram numbers in the range {} to {} is :".format(j, j + 100))
        print(new_array_anagram[i])
        i += 1

    return


def range_prime_and_anagram_generation():
    """ Function to return prime number in ranges"""
    prim_num = prime_nos_queue.print_prime()
    anagram_list = list(prime_nos_queue.check_anagrams(prim_num))
    prime_and_anagram_printing(prim_num, anagram_list)
    return


if __name__ == "__main__":
    range_prime_and_anagram_generation()
