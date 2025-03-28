# 2. Простой калькулятор:
# Напишите программу-калькулятор, которая выполняет одну из операций (+, -, *, /) над двумя введенными пользователем числами.

def calculate(operand1, operand2, operation):
    match operation:
        case "+": return operand1+operand2
        case "-": return operand1-operand2
        case "*": return operand1*operand2
        case "/": return operand1/operand2

def act():
    operations = ["+", "-", "*", "/"]
    print("Введите первое число")
    num1 = float(input("> "))
    print("Введите второе число")
    num2 = float(input("> "))
    print("Введите знак операции (+, -, *, /)")
    op = input("> ")
    if operations.count(op)<1:
        print("Введен неизвестный тип операции")
        return
    else:
        print(f"{num1} {op} {num2} = {calculate(num1,num2, op)}")

if __name__=="__main__":
    act()