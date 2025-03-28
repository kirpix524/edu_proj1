def greet_user():
    try:
        name = input("Введите ваше имя: ")
        age = int(input("Введите ваш возраст: "))

        days = age * 365
        hours = days * 24
        seconds = hours * 3600

        print(f"Привет {name}! Тебе {age} лет, {days} дней, {hours} часов, {seconds} секунд.")
    except ValueError:
        print("Ошибка: введите корректный возраст!")


if __name__ == "__main__":
    greet_user()
