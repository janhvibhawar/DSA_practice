
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        else:
            temp = self.top
            popped_data = temp.data
            self.top = self.top.next
            temp = None
            return popped_data

    def print(self):
        temp = self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp = temp.next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None

        temp = self.front
        dequeued_data = temp.data
        self.front = temp.next

        if self.front is None:
            self.rear = None

        temp = None
        return dequeued_data

    def printQueue(self):
        temp = self.front
        print("Queue elements...")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def reverse_stack(s1):
    q1 = Queue()

    # Step 1: Pop from Stack and Enqueue into Queue
    while not s1.isempty():
        q1.enqueue(s1.pop())

    # Step 2: Dequeue from Queue and Push into Stack
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))

    # Display reversed Stack
    print("\nAfter reversing Stack:")
    s1.print()


# Main Program

st = stack()

st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))

print("Original Stack:")
st.print()
reverse_stack(st)
