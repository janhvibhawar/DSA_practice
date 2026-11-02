stack = []

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Popped element:", stack.pop())

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements (Top to Bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

def reverse_string():
    string = input("Enter a string: ")
    temp = []

    for ch in string:
        temp.append(ch)

    reversed_string = ""

    while len(temp) > 0:
        reversed_string += temp.pop()

    print("Reversed string:", reversed_string)

def reverse_stack():
    if len(stack) == 0:
        print("Stack is empty")
        return

    temp = []

    while len(stack) > 0:
        temp.append(stack.pop())

    print("Stack reversed successfully")
    for i in range(len(temp)-1,-1,-1):
        print(temp[i])

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        reverse_string()
    elif choice == 5:
        reverse_stack()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")