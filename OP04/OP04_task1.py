# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.
def sum_range(start, end):
    result=0
    for i in range(start, end+1, 1):
        result=result+i
    return result

print("введите начало диапазона")
start_d = int(input("> "))
print("введите конец диапазона")
end_d = int(input("> "))

if start_d>end_d:
    print("Конец диапазона не может быть меньше начала")
else:
    print(f"сумма = {sum_range(start_d,end_d)}")