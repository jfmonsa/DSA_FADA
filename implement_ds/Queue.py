class Queue:
    """Implementación de una cola circular"""
    def __init__(self, lenght):
        self.items = []
        self.lenght=lenght
        self.head = 0
        self.tail = 0

    def enqueue(self, key):
        """
        Encolar, agrega un elemento a la cola en el extremo
        llamado tail
        """
        if self.is_full():
            raise ValueError("La cola está llena")
        #idea: self.items.append(key)
        self.items[self.tail] = key
        self.tail = (self.tail + 1) % len(self.items)

    def dequeue(self):
        """
        Desencolar, elimina un elemento de la cola
        en el extremo llamado head
        """
        if self.is_empty():
            raise ValueError("La Cola esta vacia")
        #return self.items.pop(0)
        dequeued = self.items[self.head]=None
        self.head = (self.head + 1) % len(self.items)
        #self.__size -= 1
        return dequeued

    def is_empty(self):
        return not self.items
    
    def is_full(self):
        return self.tail==self.head
    
"""
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)
"""