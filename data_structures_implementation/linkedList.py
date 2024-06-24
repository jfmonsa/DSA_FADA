"""
Implementation of Single Linked List
"""


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # initializes the linked list with an empty head
        self.head = None

    def size(self):
        count = 0
        if not self.head:
            return 0
        else:
            current_node = self.head
            while current_node:
                count += 1
                current_node = current_node.next
            return count

    def search(self, elm):
        if self.size() > 0:
            count = 0
            current_node = self.head
            while current_node:
                if current_node.data == elm:
                    # returnning the index of the element
                    return count
                count += 1
            return None
        else:
            raise Exception("No elements in the Linked List")

    # Insertion
    def insertAtStart(self, data):
        new_node = LinkedListNode(data)
        if self.head == None:
            self.head == new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = LinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insertAtPos(self, data, pos):
        if pos == 0:
            self.insertAtStart(data)
            return

        new_node = LinkedListNode(data)
        count = 0
        current_node = self.head

        while current_node and count < pos - 1:
            count += 1
            current_node = current_node.next

        if current_node is None:
            raise Exception("Posición fuera de rango")

        new_node.next = current_node.next
        current_node.next = new_node

    # Update
    def updateNode(self, data, pos):
        pass

    # Deletion
    def delAtStart(self):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")
        else:
            self.head = self.head.next

    def delAtEnd(self):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delAtPos(self, pos):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")
        else:
            count = 0
            current_node = self.head
            if pos == 0:
                self.delAtStart()
            else:
                while current_node and count + 1 != pos:
                    current_node.next = current_node.next.next
                # Change pointers here
                if current_node:
                    current_node.next = current_node.next.next
                else:
                    raise Exception("OutOfIndex: error index not present")


if "__main__" == __name__:
    pass
