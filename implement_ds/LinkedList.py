from implement_ds.DynamicSets import DynamicSet

class Node:
    def __init__(self, key):
        self.key : any = key #node value (data)
        self.next : Node = None #next node

class LinkedList(DynamicSet): #Heredar nodo aquí Node? 
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

        #TODO: podemos implementar el tail tambien

    """
        https://github.com/GreatHayat/LinkedList-Python/blob/master/linked_list.py
    """
    #append
    #search
    #head
    #tail
    #next
    #insert
    def is_empty(self)->bool:
        return self.head is None

    def append(self,key):
        new_node = Node(key)

        if self.is_empty():
            self.head = new_node
        else:
            #traverse till last node
            current_node = self.head
            while not current_node.next is None:
                current_node = current_node.next
            #when the last node is empty append the new node
            current_node.next= new_node
            #self.tail=new_node

    def search(self,key):
        x=self.head
        while x!=None:
            if x.key==key:
                return x
            x=x.next

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