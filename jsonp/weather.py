    # Create a linked list class
class LinkedList:

    # Initialize the linked list with a head node
    def __init__(self, head):
        self.head = head

    # Add a new node to the linked list
    def add(self, node):
        # If the linked list is empty, make the new node the head node
        if self.head is None:
            self.head = node
        else:
            # Find the last node in the linked list
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            # Set the last node's next pointer to the new node
            last_node.next = node

    # Get the length of the linked list
    def get_length(self):
        # Initialize a counter to track the length of the linked list
        length = 0

        # Start at the head node and iterate through the linked list
        current_node = self.head
        while current_node is not None:
            # Increment the counter by 1
            length += 1

            # Move on to the next node
            current_node = current_node.next

        # Return the length of the linked list
        return length

    # Print the contents of the linked list
    def print(self):
        # Start at the head node and iterate through the linked list
        current_node = self.head
        while current_node is not None:
            # Print the current node's data
            print(current_node.data)

            # Move on to the next node
            current_node = current_node.next