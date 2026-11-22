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

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, "=>", end="")
            temp = temp.next
        print("None")

    def deleteHead(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            self.head = self.head.next

s1 = SinglyLinkedList()

s1.insert(Node(100))
s1.insert(Node(200))
s1.insert(Node(300))
s1.insert(Node(400))

print("\nOriginal Linked List:")
s1.print()

print("\nAfter deleting head node:")
s1.deleteHead()
s1.print()



