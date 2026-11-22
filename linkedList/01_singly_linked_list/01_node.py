class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


#Creating individual nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

#Connecting nodes
n1.next = n2
n2.next = n3

head = n1

print(head.data)
print(head.next.data)
print(head.next.next.data)
