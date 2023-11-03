from imports import *

#Auxiliary operations
def precedence(op:str)->int:
        PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '%':2, '^': 3}
        return PRECEDENCE[op]

def is_operator(char:str)->bool:
        return char in "+-*/^%"


"""
(1)
Description: Conversion between aritmethic notations: postfix, prefix and infix

*) La idea general es que en postfijo los operadores que aparecen primero tienen
mayor prioridad

*) You can convert directly moving the operator within the brackets
e.g. (X + Y) or (X Y +) or (+ X Y). and finally remove any superfluous brackets.

TODO: implementar unit-testing
#post->inf pre | inf-> post pre | pre->int post
"""

#test_expressions
infix_exps = ["3+4*(2-1)",
            "((A+B)-C*(D/E))+F",
            "(5+3)*8-4",
            '4*2+5*(2+1)/2',
            'A*(B+C)/D'
            ]

prefix_exps=["*+A B-C D",
             "*-A/B C-/A K L"]

postfix_exprs=["A B+C D-*",
               "A B C/-A K/L-*",
               "a b c++",
               "a b*c+" ]

#infix to postfix
def infix_2_postfix(infix_exp :str)->str:
    
    """Convert infix to postfix exp."""

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

"""
#test
for exp in expressions:
    infix_2_postfix(exp)
"""

#prefix to postfix
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
    
"""
#test
for exp in prefix_exps:
    prefix_to_infix(exp)
"""

#prefix to postfix
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

"""
#test
for exp in prefix_exps:
    prefix_2_postfix(exp)
"""

#postfix to prefix
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

"""
#test
for exp in postfix_exprs:
    postfix_2_prefix(exp)
"""

#postfix to infix
def postfix_2_infix(postfix_exp:str)->str:
    tokens = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\^\+\*\-\/])", postfix_exp)
    s=Stack(len(tokens)) #fill with operators
    prefix=""

    for token in tokens:
        if token.isalnum():
            s.push(token)
        elif is_operator(token):
            if s.size() >=2:
                operand_a=s.pop()
                operand_b=s.pop()
                s.push("("+operand_a+token+operand_b+")")
            else:
                raise Exception("Expresión no válida")
        else:
            raise Exception("Expresión no válida")   

    if s.size()==1:
        infix = s.pop()
        print(f"postfix: {postfix_exp} -> infix: {infix}")
        return infix
    else:
        raise Exception("Expresión invalida")

"""
#test
for exp in postfix_exprs:
    postfix_2_infix(exp)
"""

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

"""
(2) Parentheses managing problems
"""

def is_balanced(str: str)->bool:

    """ Vefify if a given arithmethic expression has balanced parentheses."""

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

"""
#tests
#print(is_balanced("4*[5+(3-{5+2})]")) #balanced
#print(is_balanced("4*[5+(3-{5+2}){]]")) #not balanced
#print(is_balanced("{4+[[5)")) #not balance
"""

#method to delete superflous parentheses

"""
(3) Eval arithmethic expressions
"""
#postfix
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

#prefix
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

#infix
"""
implement a function to evaluate infix arithmetic, expressions:
https://en.wikipedia.org/wiki/Shunting_yard_algorithm
"""

def eval_infix(exp:str)->int:
    tokens=re.findall(r"\b\w+[\.]?\w*\b|[\+\-\*\/\%\^\)\(]",exp)
    s_operands=Stack(len(exp))
    s_operators=Stack(len(exp))

    for token in tokens:
        #Me siento orgulloso pq deduje toda la parte de los 3 primeros condicionalees :D
        # ")" "(" y isdecimal()

        if token.isdecimal():
            s_operands.push(token)
        elif token=="(":
            s_operators.push()
        elif token==")":
            if s_operands.size()>=2:
                op_a=s_operands.pop()
                op_b=s_operands.pop()
                operator=s_operators.pop()
                s_operands.push(eval(op_a+operator+op_b))
                s_operators.pop() #delete opening parentheses
            else:
                raise Exception("Expresion no valida")

        elif is_operator(token):
            #Para este condicional si me tocó consultar el algoritmo xd
            #token is the current operator
            #s_operators.top() is the previous operator
            #if prev operator <= current operator
            while not s_operators.is_empty() and precedence(s_operators.top())<=precedence(token):
                op_a=s_operands.pop()
                op_b=s_operands.pop()
                s_operands.push(eval(op_a+operator+op_b))
            else:
                s_operators.push(token)
        else:
            raise Exception("Expresion invalida")
    #terminar de procesar lo que aún quede en la lista de operadores
    while not s_operators.is_empty():
        if s_operands.size()>=2:
            op_a=s_operands.pop()
            op_b=s_operands.pop()
            operator=s_operators.pop()
            s_operands.push(eval(op_a+operator+op_b))
        else:
            raise Exception("Expresion no valida")
    if s_operands.size()==1:
        result = s_operands.pop()
        print(f"The result of the given expression: {exp} is equal to: {result}")
        return result
    else:
        raise Exception("Expresión invalida")
    
#test
for exp in ["3+4*(2-1)",
            "(5+3)*8-4",
            #'4*2+5*(2+1)/2',
            ]:
    eval_infix(exp)