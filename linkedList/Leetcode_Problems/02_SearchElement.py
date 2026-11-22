class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None

    def searchKey(self, key):
        temp =self.head
        while temp is not None:
            if temp.data == key:
                print("Yes element exist in linked list")
                return
            temp=temp.next
        print("No element  does not exist in linked list")

    def print(self):
        temp = self.head
        if temp is None:
            print("Linked list is empty")
            return
        while temp is not None:
            print(temp.data, "=>", end=" ")
            temp = temp.next
        print("None")

s1 = SinglyLinkedList()

s1.insert(Node(1))
s1.insert(Node(2))
s1.insert(Node(3))
s1.insert(Node(4))

s1.print()

s1.searchKey(89)