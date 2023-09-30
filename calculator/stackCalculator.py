formular = input("Enter your formular: ")

oper = {"*":1,"/":1,"+":0,"-":0}
stack = []
number = ""

postfix = []

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


calStack = []
for c in postfix:
    if c in oper.keys():
        b,a = calStack.pop(), calStack.pop()
        if c == "*":
            calStack.append(a*b)
        elif c == "/":
            calStack.append(a/b)
        elif c == "+":
            calStack.append(a+b)
        elif c == "-":
            calStack.append(a-b)
    else:
        calStack.append(c)

print(*calStack)
