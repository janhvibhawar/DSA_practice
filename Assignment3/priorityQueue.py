class Node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):

        if self.front == None:
            self.front = self.rear = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        else:
            temp = self.front

            while temp:
                if new_node.priority < temp.priority:
                    break
                else:
                    prev = temp
                    temp = temp.next

            prev.next = new_node
            new_node.next = temp

            if temp == None:
                self.rear = new_node

    def display_next(self):
        if self.front == None:
            print("No patients waiting")
        else:
            print("Next Patient:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Patient treated:", temp.name)

            self.front = self.front.next

            if self.front == None:
                self.rear = None


    def display_all(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front

            print("\nWaiting Patients:")
            while temp:
                if temp.priority == 1:
                    p = "Critical"
                elif temp.priority == 2:
                    p = "Serious"
                else:
                    p = "Normal"

                print("ID:", temp.pid,
                      "Name:", temp.name,
                      "Priority:", p)

                temp = temp.next


pq = PriorityQueue()

while True:
    print("\n--- Hospital Emergency Management ---")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")

        print("1. Critical")
        print("2. Serious")
        print("3. Normal")

        pr = int(input("Enter Priority: "))

        if pr >= 1 and pr <= 3:
            pq.enqueue(Node(pid, name, pr))
            print("Patient added successfully")
        else:
            print("Invalid Priority")

    elif ch == 2:
        pq.display_next()

    elif ch == 3:
        pq.dequeue()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
