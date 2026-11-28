#Doubly Circular Linked List Implementation
class Node:    
    def __init__(self,value):   
        self.prev = None
        self.data = value        
        self.next = None
        
        
class DCLinkedList:
    
    def __init__(self):
        self.head = None   
        
    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next!=self.head:
                temp = temp.next
            temp.next = new_node
            new_node.prev=temp
            new_node.next=self.head
            self.head.prev=new_node
        else:
            self.head = new_node
            new_node.next=new_node.prev=self.head
            
    def print(self):
        temp = self.head
        while temp.next!=self.head:
            print(temp.data, end=" ")
            temp = temp.next 
        print(temp.data)
            
    def insert(self, new_node, position):
        count=1
        temp = temp1 = self.head
        if position == 1:
            while temp1.next!=self.head:
                temp1=temp1.next
            new_node.next = self.head
            self.head.prev=new_node
            self.head = new_node
            temp1.next=self.head
            self.head.prev=temp1
        else:
            while temp:
                if count+1 == position:
                    new_node.next =temp.next
                    new_node.prev=temp
                    if temp.next:
                        temp.next.prev=new_node
                    temp.next = new_node
                    return
                else:
                    count+=1
                    temp = temp.next
                
    def delete(self, value):
        temp = temp1 = self.head
        if temp.data == value:
            while temp1.next!=self.head:
                temp1=temp1.next
            self.head = temp.next
            self.head.prev=temp1
            temp1.next=self.head
        else:
            while True:
                if temp.data == value: #node is found
                    break
                temp = temp.next
                if temp == self.head:
                    print("Value not present")
                    return
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev=temp.prev
        temp = None
    
   
#create new linked list
llist = DCLinkedList()
n1 = Node(10)
n2 = Node(20)
llist.append(n1)
llist.append(n2)
llist.append(Node(30))
llist.print()
print("After insertion....")
llist.insert(Node(40),3)
llist.print()
llist.delete(30)
print("After deletion....")
llist.print()