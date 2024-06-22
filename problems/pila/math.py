from implement_ds.stack import Stack
import copy, re


# Auxiliary operations
def precedence(op: str) -> int:
    if is_operator(op):
        PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}
        return PRECEDENCE[op]
    elif op == "(":
        return 0


def is_operator(char: str) -> bool:
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

# test_expressions
infix_exps = [
    "3+4*(2-1)",
    "((A+B)-C*(D/E))+F",
    "(5+3)*8-4",
    "4*2+5*(2+1)/2",
    "A*(B+C)/D",
]

prefix_exps = ["*+A B-C D", "*-A/B C-/A K L"]

postfix_exprs = ["A B+C D-*", "A B C/-A K/L-*", "a b c++", "a b*c+"]

"""
#test
for exp in expressions:
    infix_2_postfix(exp)
"""

"""
implement a function to evaluate infix arithmetic, expressions:
https://en.wikipedia.org/wiki/Shunting_yard_algorithm
"""


def eval_infix(exp: str) -> int:
    tokens = re.findall(r"\b\w+[\.]?\w*\b|[\+\-\*\/\%\^\)\(]", exp)
    s_operands = Stack(len(exp))
    s_operators = Stack(len(exp))

    for token in tokens:
        # Me siento orgulloso pq deduje toda la parte de los 3 primeros condicionalees :D
        # ")" "(" y isdecimal()

        if token.isdecimal():
            s_operands.push(token)
        elif token == "(":
            s_operators.push(token)
        elif token == ")":
            if s_operands.size() >= 2:
                op_a = s_operands.pop()
                op_b = s_operands.pop()
                operator = s_operators.pop()
                s_operands.push(eval(op_a + operator + op_b))
                s_operators.pop()  # delete opening parentheses
            else:
                raise Exception("Expresion no valida")

        elif is_operator(token):
            # Para este condicional si me tocó consultar el algoritmo xd
            # token is the current operator
            # s_operators.top() is the previous operator
            # if prev operator <= current operator
            while not s_operators.is_empty() and precedence(
                s_operators.top()
            ) <= precedence(token):
                operator = s_operators.pop()
                op_a = str(s_operands.pop())
                op_b = str(s_operands.pop())
                s_operands.push(eval(op_a + operator + op_b))
            else:
                s_operators.push(token)
        else:
            raise Exception("Expresion invalida")
    # terminar de procesar lo que aún quede en la lista de operadores
    while not s_operators.is_empty():
        if s_operands.size() >= 2:
            operator = s_operators.pop()
            op_a = str(s_operands.pop())
            op_b = str(s_operands.pop())
            s_operands.push(eval(op_a + operator + op_b))
        else:
            raise Exception("Expresion no valida")
    if s_operands.size() == 1:
        result = s_operands.pop()
        print(f"The result of the given expression: {exp} is equal to: {result}")
        return result
    else:
        raise Exception("Expresión invalida")


# test
# TODO: la función esta fallando en algunos casos
"""
for exp in ["3+4*(2-1)",
            "(5+3)*8-4",
            #'4*2+5*(2+1)/2',
            ]:
    eval_infix(exp)
"""
