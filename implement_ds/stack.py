"""
Definition:
Stack is a simple linear data structure used for storing data.
Stack follows the LIFO (Last In First Out) It can be implemented through
an array or linked lists. Some of its main operations are: push(), pop(),
top(), isEmpty(), size()

Pros and Cons:
* Fast access time: O(1) primary operations
* No suitable for applications that require accessing elements in the middle of the stack,
    like searching or sorting algorithms
* Underflow or Overflow


Use - cases of stacks:
* Function calls: Stack data structure is used to store function calls and their states, which helps
    in the efficient implementation of recursive function calls.
* Supports backtracking algorithms: to explore all possible solutions by storing the previous states.
* Used in Compiler Design: for parsing and syntax analysis of programming languages.
* Expression evaluation: s used to evaluate expressions in infix, postfix, and prefix notations.
Operators and operands are pushed onto the stack, and operations are performed based on the stack's top
* Enables undo/redo operations
* Balanced Parentheses

"""

class Stack:
    """
    Stack's implementation on a list
    """
    def __init__(self,lenght:int):#,items=[]):
        self.items = []#items #empty list [] by default
        self.lenght=lenght

    def is_empty(self) -> bool:
        return not self.items
        # truth representation of list, false if is no empty

    def is_full(self) -> bool:
        return self.size()==self.lenght

    def push(self, item) -> None:
        if not self.is_full():
            self.items.append(item)
        else:
            raise Exception("Stack is full, can't push")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty, can't pop")
    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        #raise IndexError("La pila está vacía")

    def __str__ (self):
        return str(self.items)

    def size(self) -> int:
        return len(self.items)
    

#Nota: hacer otras implementaciones, de la pila

"""
(3) Maximos y minimos
Para tener el maximo elmento (más grande) y el minimo elmento (más pequeño)
de una pila con una complejidad de O(1), debemos modificar las operaciones push()
y pull(), de tal manera que cuando agreguemos los elmentos para construir la pila
vamos constuyendo otra pila auxiliar ya sea de máximos o minimos y se hace push
a esa pila auxiliar si el elmento es más grande o más pequeño según corresponda 
que la anterior
"""