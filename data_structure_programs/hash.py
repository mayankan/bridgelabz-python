from data_structure_programs.data_structures_operations.hash import Hash


def main():
    _hash = Hash()
    ans = int(input("Enter the number of values"))
    print("Enter ", ans, " value")
    for i in range(ans):
        val = int(input())
        n = _hash.Node(val)
        _hash.insert(n)
    _hash.display()


if __name__ == "__main__":
    main()