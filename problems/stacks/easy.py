from data_structures_implementation.stack import Stack
import copy

# Ejemplos
s0 = Stack(4)
s1 = Stack(6)
s1.push(1)
s1.push(23)
s1.push(3)
s1.push(61)
s1.push(2)
s1.push(10)  # top

# Ejercicios
"""
(1) Implementar un algoritmo que recibe un entero x y una pila de enteros p.
el algoritmo debe retornar una nueva pila sin el elemento x y conservando 
el mismo orden
"""


def del_stack_elm(s: Stack, x: int) -> Stack:
    print(s)
    temporal_stack = Stack(s.size())  # a new temporal Stack

    while not s.is_empty():
        tmp_elm = s.pop()
        if tmp_elm != x:
            temporal_stack.push(tmp_elm)
    # Stack whiout element but is reverse order

    while not temporal_stack.is_empty():
        s.push(temporal_stack.pop())
    return s


# testing
# del_stack_elm(s1,61)

"""
(2) hacer un algoritmo para chequear si un número es capicua, capicua, que se lee igual de derecha
a izquierda, usar pilas
"""


def is_capicua(s: Stack) -> bool:
    reverse_stack = Stack(s.lenght)
    temporal_stack = copy.deepcopy(s)
    while not temporal_stack.is_empty():
        reverse_stack.push(temporal_stack.pop())

    # verify both stacks to know if is capicua number
    while not s.is_empty():
        if s.pop() != reverse_stack.pop():
            return False
    return True


# tests
# 2992
s2 = Stack(4)
s2.push(2)
s2.push(9)
s2.push(9)
s2.push(2)
print(is_capicua(s2))
print(is_capicua(s1))
