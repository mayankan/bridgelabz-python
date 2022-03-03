class Hash:
    def __init__(self):
        node0 = Node()
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()
        node6 = Node()
        node7 = Node()
        node8 = Node()
        node9 = Node()
        node10 = Node()

        self.arr = [node0, node1, node2, node3, node4, node5, node6, node7, node8, node8, node9, node10]

    def insert(self, value):
        n = Node(value)  # create a node
        res = int(value.data % 11)  # calc hash value
        node = self.arr[res]  # node var points to array index
        if node is None:
            node = n
        else:
            ptr = self.arr[res]
            while ptr.next is not None:  # traversing to end element in link
                ptr = ptr.next
            ptr.next = n  # storing node in last position of hash index

    def display(self):
        res = None
        for i in range(len(self.arr)):
            print("Remainder", i, "has following values", end=" ")
            ptr = self.arr[i]
            if ptr == None:  # Hash value has no data
                print("None")
            else:
                while ptr.next != None:
                    print(ptr.data, end=",")  # print all values in that hash position
                    ptr = ptr.next
                    print(ptr.data)
            print()


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
