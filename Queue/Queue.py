queue = []

def enqueue():
    element = input("Enter element to insert: ")
    queue.append(element)
    print(element, "inserted into queue")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements (Front to Rear):")
        for i in range(len(queue)):
            print(queue[i])

def reverse_queue():
    if len(queue) == 0:
        print("Queue is empty")
        return

    temp = []

    while len(queue) > 0:
        temp.append(queue.pop(0))

    while len(temp) > 0:
        queue.append(temp.pop())

    print("Queue reversed successfully")
    display()

def merge_queue():
    queue2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        queue2.append(element)

    queue.extend(queue2)

    print("Queues merged successfully")
    display()

def identical_queue():
    queue2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        queue2.append(element)

    if queue == queue2:
        print("Both queues are identical")
    else:
        print("Queues are not identical")

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        reverse_queue()
    elif choice == 5:
        merge_queue()
    elif choice == 6:
        identical_queue()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
