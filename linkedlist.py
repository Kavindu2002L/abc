class Node:
    def __init__(self, data):  # Fixed constructor method name
        self.data = data        # Fixed assignment
        self.next = None

class LinkedList:
    def __init__(self):         # Fixed constructor method name
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def insert_at_beginning(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

# Creating linked list and nodes
ll = LinkedList()
ll.head = Node("Toyota")
l2 = Node("BMW")
l3 = Node("Audi")
l4 = Node("Lamborghini")       # Fixed typo: "Lambogini"

# Linking nodes
ll.head.next = l2
l2.next = l3
l3.next = l4

# Insert a new node at the beginning
ll.insert_at_beginning("Ford")

# Print the linked list
ll.listprint()