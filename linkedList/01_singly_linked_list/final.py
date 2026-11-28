#Singly Linear Linked List
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    
          
    def insert(self, new_node, pos):
        if pos==1: #insert node at first position
            new_node.next=self.head
            self.head=new_node
        else: #insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            temp.next=new_node
    def delete(self, value):
        temp=self.head
        prev=None
        if temp.data==value: #first node to delete
            self.head=self.head.next
        else:
            while(temp.data!=value and temp):
                prev=temp
                temp=temp.next
                if temp==None:
                    print("Value is not present in the list")
                    return
            prev.next=temp.next
            temp=None

           
    def print(self):
        print("List elements: ")
        temp=self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next

list1=LinkedList()
n1=Node(10)
n2=Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(55))
list1.append(Node(65))
list1.print()
list1.insert(Node(34),7)
list1.print()
list1.delete(650)
list1.print()
