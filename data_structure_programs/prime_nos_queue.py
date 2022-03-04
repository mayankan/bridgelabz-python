import data_structures_operations.queue as queue


def print_prime():
    """
    program to print prime numbers from 0 to 1000
    :return:
    """
    prime_lis = []
    for num in range(0, 1000 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_lis.append(num)
    return prime_lis


def check_anagrams(l):
    """checking whether the number is anagram or not"""
    ana = set()
    cou = 0
    for i in l:
        j = str(i)
        k = sorted(j)
        for j in [x for x in l[cou + 1:len(l)]]:
            h = str(j)
            m = sorted(h)
            if k == m:
                ana.add(i)
                ana.add(j)
        cou += 1
    return ana


def anagram_and_dictform(dicti):
    dicti = sorted(dicti)
    liss = []
    for i in dicti:
        j = i + 1
        for j in dicti:
            if i == j:
                pass
            elif sorted(str(i)) == sorted(str(j)):
                liss.append({i: j})
            else:
                pass
    for j in liss:
        inv_map = {v: k for k, v in j.items()}
        if inv_map in liss:
            liss.remove(j)
    for j in liss:
        inv_map = {v: k for k, v in j.items()}
        if inv_map in liss:
            liss.remove(j)
    return liss


def linked_list_operation(liss):
    llist = queue.Queue()
    for i in liss:
        llist.en_queue(i)
    return llist


def linked_list_removal(_list):
    num = int(input("Enter the number of elements that you want to remove : "))
    for i in range(0, num):
        _list.de_queue()
    return _list


if __name__ == "__main__":
    prim_num = print_prime()
    dicti = check_anagrams(prim_num)
    list_anagrams = anagram_and_dictform(dicti)
    que_llist = linked_list_operation(list_anagrams)
    dequed_list = linked_list_removal(que_llist)
    que_llist.print_list()
