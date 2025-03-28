def calculate_rectangle_area():
    try:
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))

        area = length * width
        print(f"Площадь прямоугольника: {area}")
    except ValueError:
        print("Ошибка: введите корректные числа!")


if __name__ == "__main__":
    calculate_rectangle_area()