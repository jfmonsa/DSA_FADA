from data_structures_implementation.stack import Stack

"""
Excercises 1:
Main concepts: prefix (polish), infix, postfix (reverse-polish) notations
"""


# Aux funcions
def opPrecedence(operator: str):
    prec = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
    if operator in prec:
        return prec[operator]
    else:
        raise Exception("Unknown operator")


def opAssociativity(operator: str):
    return "RIGHT" if operator == "^" else "LEFT"


def isOperand(ch: str) -> bool:
    return ch.isalpha() or ch.isdigit()


def isOperator(token: str) -> bool:
    return token in "^*/+-"


def doMath(op, left, right):
    if op == "^":
        return left**right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right
    elif op == "+":
        return left + right
    elif op == "-":
        return left - right
    else:
        raise ValueError(f"Unknown operator: {op}")


"""
# 1
Write a program to convert an Infix expression to Postfix form.

E.g:
    Input: A + B * C + D
    Output: ABC*+D+
"""


def infixToPostfix(exp: str) -> str:
    stack = Stack()
    postfixExp = ""

    for ch in exp:
        if isOperand(ch):
            postfixExp += ch
        elif ch == "(" or stack.isEmpty():
            stack.push(ch)
        elif ch == ")":
            while stack.peek() != "(":
                postfixExp += stack.pop()
            # pop remaining "(" in stack
            stack.pop()
        elif isOperator(ch):
            while (
                (not stack.isEmpty())
                and stack.peek() != "("
                and (
                    (opPrecedence(ch) < opPrecedence(stack.peek()))
                    or (
                        opAssociativity(ch) == "LEFT"
                        and opPrecedence(ch) == opPrecedence(stack.peek())
                    )
                )
            ):
                # pop and append to postfix exp higher priority operators
                postfixExp += stack.pop()
            # then push less priority operator
            stack.push(ch)
    while not stack.isEmpty():
        postfixExp += stack.pop()
    return postfixExp


def prefixToInfix(exp: str) -> str:
    # Save operands in a stack
    tokenList = exp.split()
    stack = Stack()

    i = len(tokenList) - 1
    while i >= 0:
        if isOperand(tokenList[i]):
            stack.push(tokenList[i])
        elif stack.size() >= 2:
            stack.push("(" + str(stack.pop()) + tokenList[i] + str(stack.pop()) + ")")
        i -= 1
    return stack.pop()


def prefixToPostfix(exp: str) -> str:
    tokenList = exp.split()
    stack = Stack()

    i = len(tokenList) - 1
    while i >= 0:
        if isOperand(tokenList[i]):
            stack.push(tokenList[i])
        elif isOperator(tokenList[i]) and stack.size() >= 2:
            stack.push(f"{stack.pop()} {stack.pop()} {tokenList[i]}")
        i -= 1
    return stack.pop()


def postfixToPrefix(exp: str) -> str:
    tokenList = exp.split()
    stack = Stack()

    for token in tokenList:
        if isOperand(token):
            stack.push(token)
        elif isOperator(token) and stack.size() >= 2:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.push(f"{token} {op1} {op2}")
    return stack.pop()


# TODO: postfixToInfix
# TODO: infixToPrefix
"""
TODO:

implement a function to evaluate infix arithmetic, expressions:
https://en.wikipedia.org/wiki/Shunting_yard_algorithm
"""


def validateParentheses(exp: str) -> bool:
    """
    Validate parentheses of an infix exp
    """
    stack = Stack()

    for ch in exp:
        if ch in ["(", "{", "["]:
            stack.push(ch)
        elif stack.isEmpty():
            return False
        elif ch == ")":
            if stack.peek() != "(":
                return False
            stack.pop()
        elif ch == "]":
            if stack.peek() != "[":
                return False
            stack.pop()
        elif ch == "}":
            if stack.peek() != "{":
                return False
            stack.pop()
    return stack.isEmpty()


def evalPostfix(exp: str) -> int:
    stack = Stack()
    tokenList = exp.split()

    for token in tokenList:
        if token.isdigit():
            stack.push(token)
        elif stack.size() >= 2:
            r = int(stack.pop())
            l = int(stack.pop())
            stack.push(doMath(token, l, r))
    return stack.pop()


def evalPrefix(exp: str) -> int:
    stack = Stack()
    tokenList = exp.split()

    for token in reversed(tokenList):
        if isOperand(token):
            stack.push(token)
        elif isOperator(token) and stack.size() >= 2:
            stack.push(doMath(token, int(stack.pop()), int(stack.pop())))
    return stack.pop()


if __name__ == "__main__":
    print(infixToPostfix("a+b*c+d"))
    print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))
    print(validateParentheses("a+b*(c^d-e)^(f+g*h)-i"))
    print(evalPostfix("2 2 + 3 * 10 -"))
    print(prefixToInfix("* - A / B C - / A K L"))
    print(prefixToPostfix("* - A / B C - / A K L"))
    print(postfixToPrefix("a b c / - a d / e - *"))
    print(evalPrefix(postfixToPrefix("2 2 + 3 * 10 -")))
    # TODO: implementar unit-testing
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
