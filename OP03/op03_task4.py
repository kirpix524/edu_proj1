# 4. Проверка на четность чисел в диапазоне:
# Напишите программу, которая принимает от пользователя два числа (начало и конец диапазона) и выводит все четные числа в этом диапазоне с помощью цикла for
def get_even_numbers(start, end):
    result=[]
    for i in range(start,end,1):
        if i % 2 == 0: result.append(i)
    return result

print("Введите начало диапазона")
start = int(input("> "))
print("Введите конец диапазона")
end = int(input("> "))
if end<start:
    print("Конец должен быть больше начала")
else:
    print(f"Четные числа в диапазоне от {start} до {end}: {get_even_numbers(start, end)}")

