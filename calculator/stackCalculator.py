import Calculator

formular = Calculator.inputFormular()
oper = {"*":1,"/":1,"+":0,"-":0}
postfix = Calculator.convertToPostfix(formular,oper)
answer = Calculator.calculatePostfix(postfix,oper)

print(*answer)
