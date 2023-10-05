def inputFormular():
    formular = input("Enter your formular: ")
    return formular


def convertToPostfix(formular,oper):
    number = ""
    postfix = []
    stack = []
    for s in formular:
        if s in oper.keys():
            postfix.append(int(number))
            while stack:
                if oper[stack[-1]] < oper[s]:
                    break
                else:
                    postfix.append(stack.pop())

            stack.append(s)
            number = ""
        else:
            number += s
    postfix.append(int(number))
    while stack:
        postfix.append(stack.pop())
    return postfix

def calculatePostfix(postfixFormular,oper):
    calStack = []
    for c in postfixFormular:
        if c in oper.keys():
            b, a = calStack.pop(), calStack.pop()
            if c == "*":
                calStack.append(a * b)
            elif c == "/":
                calStack.append(a / b)
            elif c == "+":
                calStack.append(a + b)
            elif c == "-":
                calStack.append(a - b)
        else:
            calStack.append(c)
    return calStack
