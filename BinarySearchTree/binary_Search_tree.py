class Node:
    def __init__(self,value):
        self.left = None         #left side of node 
        self.data = value       
        self.right = None        # right side of node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,new_node):
        if self.root is None:     #check if tree is empty if yes new_node becomes root , creating root node
            self.root = new_node
            return 

        else:
            temp = self.root   #we need to traverse tree to find correct position for new_node ,so we cant loose root value so we are storing it 

            while True:        #cause we dont need how many iterations it will take to find correct position
                if new_node.data < temp.data:        #for left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return    #once node is inserted successfully we can return   
                    else:         #if it is not empty we will travel next branch 
                        temp=temp.left
                elif new_node.data >=temp.data:            #for right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self,temp):  #recursive method
        if temp is None:
            return
        else:
            self.inorder(temp.left)  
            print(temp.data,end=" ")
            self.inorder(temp.right)

    def preorder(self, temp):
        if temp is None:
            return
        else:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self, temp):
        if temp is None:
            return
        else:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")

BST=BinarySearchTree()
BST.insert(Node(100))
BST.insert(Node(10))
BST.insert(Node(450))
BST.insert(Node(0))
BST.insert(Node(65))
BST.insert(Node(300))

print("\nInorder: ")
BST.inorder(BST.root)

print("\nPreorder: ")
BST.preorder(BST.root)

print("\nPostorder: ")
BST.postorder(BST.root)
