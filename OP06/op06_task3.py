#Напишите программу, которая эмулирует выбор без повторений: из списка учащихся класса программа случайным образом выбирает
# 5 уникальных имён, которые будут отвечать на уроке. Имена учащихся считываются заранее из входного списка и не должны повторятся.
from random import shuffle

def load_names(file_name):
    list_names=[]
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip()
            if line not in list_names:
                list_names.append(line)
    return list_names



names = load_names("names.txt")
for i in range(5):
    shuffle(names)
    name=names.pop()
    print(f"{i+1} имя: {name}")