from implement_ds.DynamicSets import DynamicSet

class Node:
    def __init__(self, key):
        self.key : any = key #node value
        self.next : Node = None #next node

class LinkedList(DynamicSet): #Heredar nodo aquí Node? 
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    """
        https://github.com/GreatHayat/LinkedList-Python/blob/master/linked_list.py
    """

    def append(self,key):
        """Add a Node at the end of the list"""

        new_node=Node(key)

        #si la lista esta vacia
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        # Else traverse till the last node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next

            #Change the next of last node
            last_node.next = new_node
            self.tail=new_node


    def search(self,key):
        x=self.head
        while x!=None and x!=self.key:
            pass

    """
    def list_search(self,data): #append
        x=self.head
        while x!=None and x!=self.data
    """

"""
    def insert(self, data, after_node):
        new_node = Node(data)
        new_node.next_node = after_node.next_node
        after_node.next_node = new_node

    def remove(self, node):
        if node is self.head:
            self.head = node.next_node
        else:
            previous_node = self.head
            while previous_node.next_node != node:
                previous_node = previous_node.next_node

            previous_node.next_node = node.next_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node

"""