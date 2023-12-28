# Define a class to represent a Node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a class to represent the Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Function to delete a node with a given data value
    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            return

        prev.next = current.next
        current = None

    # Function to traverse and print the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Function to take multiple inputs from the user to create the linked list
def create_linked_list():
    linked_list = LinkedList()
    num_nodes = int(input("Enter the number of nodes: "))

    for i in range(num_nodes):
        data = int(input(f"Enter data for node {i + 1}: "))
        linked_list.insert_at_end(data)

    return linked_list

# Main function to interact with the user
if __name__ == "__main__":
    linked_list = create_linked_list()

    while True:
        print("\nOptions:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Delete a node")
        print("4. Traverse and display")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter data to insert at the beginning: "))
            linked_list.insert_at_beginning(data)
        elif choice == '2':
            data = int(input("Enter data to insert at the end: "))
            linked_list.insert_at_end(data)
        elif choice == '3':
            data = int(input("Enter data to delete: "))
            linked_list.delete(data)
        elif choice == '4':
            print("\nLinked List:")
            linked_list.traverse()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
