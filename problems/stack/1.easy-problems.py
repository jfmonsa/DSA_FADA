from imports import *

#Ejemplos
s0=Stack(4)
s1=Stack(6)
s1.push(1)
s1.push(23)
s1.push(3)
s1.push(61)
s1.push(2)
s1.push(10)#top

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
#2992
s2=Stack(4)
s2.push(2)
s2.push(9)
s2.push(9)
s2.push(2)
#print(is_capicua(s2))
#print(is_capicua(s1))


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
implement a function to evaluate infix arithmetic, expressions:
4*[5+(3-{5+2})]
"""
def eval_infix(exp:str)->int:
    tokens=re.findall(r"\b\w+[\.]?\w*\b|[\+\-\*\/\%\^\)\(]",exp)
    s=Stack(len(exp))

    for token in tokens:
        pass

"""
(7)
implement a function to evaluate postfix, prefix expressions,
trabaja con operadores binarios
"""
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

