# 5. Напишите свою собственную игру - камень ножницы бумага
# Игра должна идти до 3-х побед, и выводить кто победил

def identify_winner(sign1, sign2):
    if sign1==sign2:
        return 0
    elif (sign1=="камень") and (sign2=="бумага"):
        return 2
    elif (sign1 == "камень") and (sign2 == "ножницы"):
        return 1
    elif (sign1=="ножницы") and (sign2=="бумага"):
        return 1
    elif (sign1 == "ножницы") and (sign2 == "камень"):
        return 2
    elif (sign1=="бумага") and (sign2=="ножницы"):
        return 2
    elif (sign1 == "бумага") and (sign2 == "камень"):
        return 1

points1=0
points2=0
signs={1:"камень",2:"ножницы",3:"бумага"}
while True:
    print("Какой знак показал первый игрок? 1-камень 2-ножницы 3-бумага")
    sign1 = int(input("> "))
    if signs.get(sign1) is None:
        print("введено некорректное значение")
        continue
    print("Какой знак показал второй игрок? 1-камень 2-ножницы 3-бумага")
    sign2 = int(input("> "))
    if signs.get(sign2) is None:
        print("введено некорректное значение")
        continue
    winner=identify_winner(signs.get(sign1), signs.get(sign2))
    if winner==1:
        print("Очко первому игроку!")
        points1=points1+1
    elif winner==2:
        print("Очко второму игроку!")
        points2 = points2+1
    else:
        print("Очко не получает никто!")
    if points1==3:
        print(f"Победил первый игрок со счетом {points1} : {points2}")
        break
    elif points2==3:
        print(f"Победил второй игрок со счетом {points1} : {points2}")
        break
    else:
        print(f"Счет {points1} : {points2}, игра продолжается")
