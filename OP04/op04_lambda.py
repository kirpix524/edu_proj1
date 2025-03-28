from functools import reduce


def task1():  # Используйте лямбда-функцию для вычисления квадрата каждого числа в списке numbers
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(f"squares = {list(map(lambda x: x**2, numbers))}")

def task2():  #Отфильтровать чётные числа из списка.
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(f"evens = {list(filter(lambda x: x%2==0, numbers))}")

def task3(): #Найти сумму всех элементов в списке.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"sum = {reduce(lambda s,x: s+x, numbers)}")

def task4(): #Отсортировать список по модулю чисел
    numbers = [10, 12, 3, -4, -51, 6, 72, 18, 9, 10]
    print(f"sorted = {sorted(numbers, reverse=True, key=lambda x: abs(x))}")

def task5(): #Найти максимальное значение в списке строк по длине.
    strings = ["1sdfsdfas", "wdfkjwflwjflwfj", "cwdcedci", "asdwfwfwefwdcefew", "qfwdfegewdcrgnyu"]
    print(f"max_len = {max(strings, key=lambda x: len(x))}")

def task6(): #Преобразовать список строк в список их длин.
    strings = ["1sdfsdfas", "wdfkjwflwjflwfj", "cwdcedci", "asdwfwfwefwdcefew", "qfwdfegewdcrgnyu"]
    print(f"lengths = {list(map(lambda x: str(x)+" ("+str(len(x))+")", strings))}")

task6()