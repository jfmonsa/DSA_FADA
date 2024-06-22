from data_structures_implementation.stack import Stack

"""
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
        elif ch in ["^", "*", "/", "+", "-"]:
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


if __name__ == "__main__":
    print(infixToPostfix("a+b*c+d"))
    print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))
    print(validateParentheses("a+b*(c^d-e)^(f+g*h)-i"))
    print(evalPostfix("2 2 + 3 * 10 -"))
