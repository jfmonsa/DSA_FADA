"""
Implementation of Single Linked List
"""


class SingleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


# Corregido el nombre de la clase (cambiado 'LInked' a 'Linked')
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def search(self, value):
        index = 0
        current_node = self.head
        while current_node:
            if current_node.data == value:
                return index
            index += 1
            current_node = current_node.next
        return None

    # insertion
    def insertAtStart(self, data):
        node = SingleLinkedListNode(data)
        node.next = self.head
        self.head = node

    def insertAtEnd(self, data):
        node = SingleLinkedListNode(data)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def insertAtPos(self, data, pos):
        if pos == 0:
            self.insertAtStart(data)
            return  # Añadido return para salir de la función después de insertar al inicio
        elif pos < 0:
            raise Exception("Out of index for Linked List")
        count = 0
        node = SingleLinkedListNode(data)
        current_node = self.head
        while current_node and count < pos - 1:
            current_node = current_node.next
            count += 1

        if current_node is None:
            raise Exception("Out of index exception for Linked List")
        # Corregida la condición (eliminado 'if count == pos:')
        node.next = current_node.next
        current_node.next = node

    # update
    def updateNode(self, data, pos):
        if self.head is None:
            raise Exception("Empty LinkedList")

        count = 0
        current_node = self.head
        while current_node and count != pos:
            current_node = current_node.next
            count += 1

        if current_node is None:
            raise Exception("Out of index error")

        current_node.data = data

    # deletion
    def delAtStart(self):
        if self.head is None:
            raise Exception("List already empty!")

        self.head = self.head.next

    def delAtEnd(self):
        if self.head is None:
            raise Exception("List already empty!")

        # if LinkedList is size 1
        if self.head.next is None:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def delAtPos(self, pos):
        if self.head is None:
            raise Exception("LinkedList already empty")
        if pos == 0:
            self.delAtStart()
            return  # Añadido return para salir de la función después de eliminar al inicio
        count = 0
        current_node = self.head
        while current_node and count < pos - 1:
            count += 1
            current_node = current_node.next

        if (
            current_node is None or current_node.next is None
        ):  # Añadida verificación para current_node.next
            raise Exception("Out of index")

        current_node.next = current_node.next.next

    def __str__(self):
        str_aux = ""
        current_node = self.head
        while current_node:
            str_aux += f"{current_node.data} -> "
            current_node = current_node.next
        str_aux += "null"  # Eliminado el espacio antes de "null"
        return str_aux


# Corregida la condición del if
if __name__ == "__main__":

    def main():
        lst1 = SingleLinkedList()  # Corregido el nombre de la clase
        lst1.insertAtStart(3)
        lst1.insertAtStart(2)
        lst1.insertAtPos(10, 2)
        lst1.insertAtEnd(4)
        lst1.insertAtEnd(5)
        lst1.insertAtEnd(25)
        print(lst1)
        lst1.delAtEnd()
        lst1.delAtStart()
        print(lst1)
        lst1.updateNode(32, 0)
        lst1.delAtPos(3)
        print(lst1)

    main()
