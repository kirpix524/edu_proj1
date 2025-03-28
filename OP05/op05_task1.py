# Задание 1: Базовая обработка исключений
# Напиши функцию safe_divide, которая принимает два аргумента: a и b. Функция должна пытаться делить a на b и возвращать результат. Если произойдет ошибка деления на ноль (ZeroDivisionError), функция должна возвращать None вместо возникновения исключения.
# Продемонстрируй работу функции на нескольких примерах, включая деление на ноль.

def safe_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Нужно вводить число, попробуйте еще раз!")

def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

arg1 = safe_input("Введите делимое: ")
arg2 = safe_input("Введите делитель: ")
res = safe_divide(arg1, arg2)
if res is None:
    print(f"Невозможно разделить {arg1} на {arg2}")
else:
    print(f"Результат деления {arg1} на {arg2} равен {res}")
