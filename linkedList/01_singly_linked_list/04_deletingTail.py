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
            new_node.next  = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.next = None

    def deleteTail(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "=>", end=" ")
            temp = temp.next
        print("None")


s1 = SinglyLinkedList()

s1.insert(Node(12))
s1.insert(Node(5))
s1.insert(Node(30))
s1.insert(Node(4))

print("\nOriginal Linked List:")
s1.print()

print("\nAfter deleting tail node:")
s1.deleteTail()
s1.print()



