from .linkedList import SingleLinkedListNode


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    """
    Approach:
    rear is the last node of the linked list:
    then, we enqueue at the start and dequeue at the end

    4<-3<-2  (linked list)

    2 will be front (dequeue)
    4 will be our rear element (enqueue)
    so rear.next is the new rear
    """

    def enqueue(self, item):
        new_node = SingleLinkedListNode(item)

        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue already empty")
        item = self.front.data
        self.front = self.front.next
        if self.rear is None:
            self.rear = None
        return item

    def frontNode(self):
        if self.isEmpty():
            raise Exception("Queue already empty")
        return self.front.data

    def rearNode(self):
        if self.isEmpty():
            raise Exception("Queue already empty")
        return self.rear.data

    def size(self):
        count = 0
        current_node = self.front
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self):
        output = "(front) ["
        current_node = self.front
        while current_node.next:
            output += f"{str(current_node.data)} <- "
            current_node = current_node.next
        output += f"{str(current_node.data)} ] (rear)"
        return output


if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print(q1)
    print(q1.frontNode())
    print(q1.rearNode())
    print(q1.dequeue())
