
def safe_input_num(type_name, plus_only, not_zero, message):
    while True:
        input_value = 0
        try:
            match type_name:
                case "float": input_value=float(input(message))
                case "int": input_value=int(input(message))
        except ValueError:
            match type_name:
                case "float":
                    print("Некорректное значение, нужно вводить целое или дробное число")
                case "int":
                    print("Некорректное значение, нужно вводить целое число")
                case "str":
                    print("Некорректное значение, нужно ввести текст")
            continue
        if plus_only and (input_value <= 0):
            print("Введенное значение должно быть больше нуля!")
        elif not_zero and (input_value == 0):
            print("Введенное значение не должно быть равно нулю!")
        else:
            return input_value

def check_str(string, allowed_chars):
    lst = list(string)
    for char in lst:
        if char not in allowed_chars:
            return 0
    return 1

def safe_input_file_name(message):
    allowed_chars = "., 1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXUZ_АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    while True:
        try:
            input_value = str(input(message))
        except ValueError:
            print("Некорректное значение, нужно вводить текст")
            continue
        except Exception as e:
            print(f"Ошибка: {type(e).__name__}, {e.args}")
            continue

        if check_str(input_value,allowed_chars)!=1:
            print("В имени файла должны быть только цифры, русские и английские буквы, пробел и символ подчеркивания")
            continue
        return input_value


