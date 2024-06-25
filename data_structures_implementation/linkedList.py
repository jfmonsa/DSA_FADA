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
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search(self, elm):
        count = 0
        current_node = self.head
        while current_node:
            if current_node.data == elm:
                # returning the index of the element
                return count
            current_node = current_node.next
            count += 1
        return None

    # Insertion
    def insertAtStart(self, data):
        new_node = LinkedListNode(data)
        if self.head == None:
            self.head = new_node
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
        if self.head is None:
            raise Exception("Empty LinkedList")

        count = 0
        current_node = self.head
        while current_node and count != pos:
            current_node = current_node.next
            count += 1

        if current_node:
            current_node.data = data
        else:
            raise Exception("Out of index error")

    # Deletion
    def delAtStart(self):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")
        else:
            self.head = self.head.next

    def delAtEnd(self):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delAtPos(self, pos):
        if self.head is None:
            raise Exception("UnderflowError: Linked list is already empty")

        if pos == 0:
            self.delAtStart()
            return

        count = 0
        current_node = self.head
        while current_node and count < pos - 1:
            current_node = current_node.next
            count += 1

        if current_node is None or current_node.next is None:
            raise Exception("OutOfIndex: error index not present")

        current_node.next = current_node.next.next

    # method to print LinkedList
    def __str__(self):
        current_node = self.head
        str_aux = ""
        while current_node:
            str_aux += f"[{current_node.data}] -> "
            current_node = current_node.next
        str_aux += "null"
        return str_aux


if "__main__" == __name__:

    def main():
        lst1 = LinkedList()
        lst1.insertAtStart(3)
        lst1.insertAtStart(2)
        lst1.insertAtPos(10, 2)
        lst1.insertAtEnd(4)
        lst1.insertAtEnd(5)
        lst1.insertAtEnd(25)
        lst1.delAtEnd()
        lst1.delAtStart()
        lst1.updateNode(32, 0)
        lst1.delAtPos(3)
        print(lst1)

    main()
