# 1. Поиск наименьшего числа:
# Пользователь вводит три различных числа. Напишите программу, которая находит и выводит наименьшее из этих трех чисел.
def get_minimal_number(input_lst):
    result=None
    for i in input_lst:
        if result is None: result=i
        if i<result: result=i
    return result

if __name__=="__main__":
    lst=[]
    for i in range(3):
        print(f"Введите число {i+1}")
        lst.append(float(input("> ")))
    print(f"Наименьшее из введенных чисел: {get_minimal_number(lst)}")