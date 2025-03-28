from random import random

lst = []
for i in range(3):
    lst.append(i*5)

lst.insert(0,2)
lst.insert(0,1)

print(f"Исходный список:{lst}")
lst.sort(reverse=True)
print(f"Отсортированный список:{lst}")
