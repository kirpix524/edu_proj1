#Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление. Импортируйте
# модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.
from modules import inputs,arithmetic

while True:
    print("Выберите тип операции: +, -, *, /")
    operation = str(input(": "))
    if (operation=="+") or (operation=="-") or (operation=="*"):
        arg1 = inputs.safe_input_num("float", False, False, "Введите первый аргумент: ")
        arg2 = inputs.safe_input_num("float", False, False, "Введите второй аргумент: ")
        break
    elif operation=="/":
        arg1 = inputs.safe_input_num("float", False, False, "Введите первый аргумент: ")
        arg2 = inputs.safe_input_num("float", False, True, "Введите второй аргумент: ")
        break
    else:
        print("Введен неизвестный тип операции")

match operation:
    case "+":
        res=arithmetic.summ(arg1,arg2)
    case "-":
        res=arithmetic.subtract(arg1,arg2)
    case "*":
        res=arithmetic.multiply(arg1,arg2)
    case "/":
        res=arithmetic.divide(arg1,arg2)
    case _:
        res=None

print(f"{arg1} {operation} {arg2} = {res}")





