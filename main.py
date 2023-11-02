"""
Definition:
Stack is a simple linear data structure used for storing data. Stack follows the LIFO(Last In First Out)
It can be implemented through an array or linked lists. Some of its main operations are: push(), pop(),
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
import copy

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

#Ejemplos
s0=Stack(4)
s1=Stack(6)
s1.push(1)
s1.push(23)
s1.push(3)
s1.push(61)
s1.push(2)
s1.push(10) #top

#Ejercicios
"""
(1) Implementar un algoritmo que recibe un entero x y una pila de enteros p.
el algoritmo debe retornar una nueva pila sin el elemento x y conservando 
el mismo orden
"""
def del_stack_elm(s: Stack,x: int) -> Stack:
    print(s)
    temporal_stack = Stack(s.size()) #a new temporal Stack

    while not s.is_empty():
        tmp_elm=s.pop()
        if tmp_elm!=x:
            temporal_stack.push(tmp_elm)
    #Stack whiout element but is reverse order

    while not temporal_stack.is_empty():
        s.push(temporal_stack.pop())
    return s

#testing
#del_stack_elm(s1,61)

"""
(2) hacer un algoritmo para chequear si un número es capicua, capicua, que se lee igual de derecha
a izquierda, usar pilas
"""
#2992
s2=Stack(4)
s2.push(2)
s2.push(9)
s2.push(9)
s2.push(2)

def is_capicua(s: Stack) -> bool:
    reverse_stack=Stack(s.lenght)
    temporal_stack=copy.deepcopy(s)
    while not temporal_stack.is_empty():
        reverse_stack.push(temporal_stack.pop())
    
    #verify both stacks to know if is capicua number
    while not s.is_empty():
        if s.pop()!=reverse_stack.pop():
            return False
    return True    

#tests
#print(is_capicua(s2))
#print(is_capicua(s1))

"""
(3) Maximos y minimos
Para tener el maximo elmento (más grande) y el minimo elmento (más pequeño)
de una pila con una complejidad de O(1), debemos modificar las operaciones push()
y pull(), de tal manera que cuando agreguemos los elmentos para construir la pila
vamos constuyendo otra pila auxiliar ya sea de máximos o minimos y se hace push
a esa pila auxiliar si el elmento es más grande o más pequeño según corresponda 
que la anterior
"""

"""
(4) Implement an algorithm to check if a string has balanced Parentheses
"""
def is_balanced(str: str)->bool:
    s=Stack(len(str))
    for i in str:
        if i=="(" or i=="{" or i=="[":
            s.push(i)
        elif i==")":
            if "("!=s.pop():
                return False
        elif i=="]":
            if "["!=s.pop():
                return False
        elif i=="}":
            if "{"!=s.pop():
                return False
    #true if is balanced, s is empty
    return s.is_empty()

#tests
#print(is_balanced("4*[5+(3-{5+2})]")) #balanced
#print(is_balanced("4*[5+(3-{5+2}){]]")) #not balanced
#print(is_balanced("{4+[[5)")) #not balance
"""
(7)
implement a function to evaluate postfix, prefix expressions,
trabaja con operadores binarios
"""
import re
def eval_postfix(exp:str)->int:
    s=Stack(len(exp))
    tokens = exp.split()

    for token in tokens:
        #si es un numero (trabajando con un solo digito por el momento)
        if token.isdecimal():
            s.push(token)
        
        #si no es un numero, debe ser entonces un operador 
        elif re.match(r'[\+\-\*\/\%\^]',token):
            #si no hay por lo menos dos operandos almacenados en la pila
            if s.size()<2:
                print("Error: La expresion no esta bien formada")
                return 0
            #si hay dos al menos dos operandos
            else:
                operand_b=s.pop()
                operand_a=s.pop()
                partial_result=eval(f"{operand_a} {token} {operand_b}")
                s.push(partial_result)
        else:
            print("La expresion contiene un caracter no valido")
            return 0
    if s.size()==1:
        result=int(s.pop())
        return result
    else:
        print("La expresion esta mal formada")
        return 0

#test
#print(eval_postfix("8 5 3 + * 4 -"))

def eval_prefix(exp:str)->int:
    tokens=exp.split()
    l=len(tokens)
    s=Stack(l)
    
    for i in range(l):
        token=tokens[l-i-1]
        if token.isdecimal():
            s.push(token)
        elif re.match(r'[\+\-\*\/\%\^]',token):
            if s.size()<2:
                print("No es una expresión bien formadas")
                return 0
            else:
                operand_a=s.pop()
                operand_b=s.pop()
                partial_result=eval(f"{operand_a}{token}{operand_b}")
                s.push(partial_result)
        else:
            print("La expresion contiene un caracter no valido")
            return 0
    if s.size()==1:
        return int(s.pop())
    else:
        print("No es una expresión bien formada")
        return 0

#test
#print(eval_prefix("- * 8 + 5 3 4"))

"""
(6)
Write a program to convert an Infix expression to Postfix form.
    *) La idea general es que en postfijo los operadores que aparecen primero tienen
    mayor prioridad

    *) You can convert directly moving the operator within the brackets
    e.g. (X + Y) or (X Y +) or (+ X Y). and finally remove any superfluous brackets.

"""
#Auxiliary operations
def precedence(op:str)->int:
        PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '%':2, '^': 3}
        return PRECEDENCE[op]

def is_operator(char:str)->bool:
        return char in "+-*/^%"

def infix_2_postfix(infix_exp :str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", infix_exp)
    stack_op = Stack(len(tokens))
    postfix_exp = [] #result

    for token in tokens:
        #if token is and operand add to the postfix string
        if token.isalnum():
            postfix_exp.append(token)
        #push if token is "("
        elif token == "(":
            stack_op.push(token)

        #Parentheses has top precedence, evaluate first
        elif token == ")":
            while (not stack_op.is_empty()) and stack_op.top()!="(":
                postfix_exp.append(stack_op.pop())
            stack_op.pop() #poping left parentheses
        
        # Before you can push the operator onto the stack, 
        # you have to pop the stack until you find an operator
        # with a lower priority than the current operator.
        # The popped stack elements are written to output. else

        #Right associativity, por ahora solo para "^"
        #When the operator at the top of the stack and the scanned operator both are ‘^‘. In this condition,
        #the precedence of the scanned operator is higher due to its right associativity. then push the current operator
        #(token)
       
        elif is_operator(token):
            while (not stack_op.is_empty() and
                   stack_op.top()!="(" and
                   not (token=="^" and stack_op.top()=="^")  and
                   precedence(token) <= precedence(stack_op.top())):
                postfix_exp.append(stack_op.pop())

            #cuando el token actual tiene mas precedencia que los de la pila, se apila
            #O para los que tenga asociatividad por la drecha como "^"
            stack_op.push(token) 
        
        #Si la expresion contiene un caracter no valido
        else:
            raise Exception("Invalid caracter in infix expression")

    # After the entire expression is scanned, 
    # pop the rest of the stack and verify balanced parentheses
    #si estan balanceados no debe haber ningun parenthesis izquierdo en la pila
    #ya que habrían sido eliminados en los pasos anteriores
    while not stack_op.is_empty():
        if stack_op.top()=="(":
            raise Exception("Parantesis desabalanceados")
        
        #agregar a los operadores que aún estan apilados a la expresion
        postfix_exp.append(stack_op.pop())

    result = " ".join(postfix_exp)
    print(f"infix: {infix_exp} -> postfix: {result}")
    return result

#test
infix_exps = ["3+4*(2-1)",
            "((A+B)-C*(D/E))+F",
            "(5+3)*8-4",
            '4*2+5*(2+1)/2',
            'A*(B+C)/D'
            ]
"""
for exp in expressions:
    infix_2_postfix(exp)
"""

def prefix_to_infix(prefix_exp:str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", prefix_exp)
    s=Stack(len(tokens))
    infix=""

    for token in reversed(tokens):
        if token.isalnum():
            s.push(token)
        elif is_operator(token):
            operator_a=s.pop()
            operator_b=s.pop()
            s.push("("+operator_a+token+operator_b+")")
        else:
            raise Exception("Expresión invalida")
        
    if s.size()==1:
        infix = s.pop()
        print(f"prefix: {prefix_exp} -> infix: {infix}")
        return infix
    else:
        raise Exception("Expresión invalida")
    
#test
prefix_exps=["*+A B-C D",
             "*-A/B C-/A K L"]

"""
for exp in prefix_exps:
    prefix_to_infix(exp)
"""

def prefix_2_postfix(prefix_exp:str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", prefix_exp)
    s=Stack(len(tokens))
    postfix=""

    for token in reversed(tokens):
        if token.isalnum():
            s.push(token)

        elif is_operator(token):
            if s.size() < 2:
                raise Exception("Expresión no válida")
            operand1 = s.pop()
            operand2 = s.pop()
            result:str = operand1 + operand2 + token
            s.push(result)
        else:
            raise Exception("Expresión no válida")

    if s.size() == 1:
        postfix = s.pop()
        print(f"prefix: {prefix_exp} -> postfix: {postfix}")
        return postfix
    else:
        raise Exception("Expresión no válida")

#test
"""
for exp in prefix_exps:
    prefix_2_postfix(exp)
"""

def postfix_2_prefix(postfix_exp:str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", postfix_exp)
    s=Stack(len(tokens)) #fill with operators
    prefix=""

    for token in tokens:
        if token.isalnum():
            s.push(token)

        elif is_operator(token):
            if s.size()>=2:
                operand_b=s.pop()
                operand_a=s.pop()
                s.push(token+operand_a+operand_b)
            else:
                raise Exception("Expresión no válida")    
        else:
            raise Exception("Expresión no válida")
    if s.size()==1:
        prefix = s.pop()
        print(f"postfix: {postfix_exp} -> prefix: {prefix}")
        return prefix
    else:
        raise Exception("Expresión no válida")

postfix_exprs=["A B+C D-*",
               "A B C/-A K/L-*"]

for exp in postfix_exprs:
    postfix_2_prefix(exp)

#error
"""
def infix_2_prefix(infix_exp: str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", infix_exp)
    tokens = tokens[::-1] #reverse string
    stack_op = Stack(len(tokens))
    prefix_exp = [] #result

    #intercambiar los parentesis que aparecen erroneamente al reversar
    for token in tokens:
        if token == '(':
            token = ')'
        elif token == ')':
            token = '('
    #aprovechar que ya construimos la función
    prefix = infix_2_postfix("".join(tokens))
    prefix = prefix[::-1]
    print(f" infix: {infix_exp} -> prefix: {prefix_exp}")
    return prefix_exp
"""  
#error