#Doubly Linear Linked List
class Node:
    def __init__(self, value):
        self.prev=None
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self, new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp  
        else: #First node
            self.head=new_node
    def insert(self, new_node, pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            return
        else:
            p=1
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
            new_node.next=temp.next
            if temp.next:   #Last postion
                temp.next.prev=new_node
            temp.next=new_node
            new_node.prev=temp
            return
        
    def delete(self, value):
        temp=self.head
        if temp.data==value: #first node to delete
            self.head=self.head.next
            self.head.prev=None
        else:
            while(temp.data!=value and temp):
                temp=temp.next
                if temp==None:
                    print("\nValue is not present in the list")
                    return
            temp.prev.next=temp.next
            if temp.next: #Not the last node
                temp.next.prev=temp.prev
            temp=None

    def print(self):
        temp=self.head
        print("\nList elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
    def printrev(self):
            temp=self.head
            print("\nList elements:", end=" ")
            while temp.next:
                temp=temp.next
            while temp:
                print(temp.data, end=" ")
                temp=temp.prev

    def count_occ(self,num):
            temp=self.head
            cnt=0
            while temp:
                if temp.data==num:
                    cnt+=1
                temp=temp.next
            print("\nThe occurance: ", cnt)
    
    def swap(self):
        temp=node1=self.head #node1 is first node
        while temp.next:  #temp is last node
            temp=temp.next
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp

list1=LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(12))
list1.append(Node(56))
list1.append(Node(78))
list1.print()
list1.printrev()
list1.insert(Node(120),600)
list1.print()
list1.delete(50)
list1.print()
list1.swap()
list1.print()
list1.count_occ(12)