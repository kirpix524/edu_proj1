# Задание 3: Обработка исключений прошлых программ
# Возьми одну из программ, которую мы писали на прошлых уроках, продумай, какие ошибки в программе могут появляться(можно
# прям специально пробовать ее ломать) и дополни код конструкцией try-except для обработки выявленных исключений.

def count_interest(deposit, interest_rate, monthly_cap=False):
    deposit_out = deposit
    if monthly_cap==True:
        for i in range(11):
            monthly_interest = ((deposit_out * interest_rate / 100)/12)
            deposit_out = deposit_out + monthly_interest
        return deposit_out
    else:
        interest = (deposit_out * interest_rate / 100)
        deposit_out=deposit_out + interest
        return deposit_out

def safe_input(type_name, plus_only, message):
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
            continue
        if plus_only and (input_value <= 0):
            print("Введенное значение должно быть больше нуля!")
        else:
            return input_value

deposit = safe_input("float", True,"Сумма, которую вы хотите положить на счет: ")
interest_rate = safe_input("float",True,"Процентная ставка, годовых: ")
years = safe_input("int",True,"На сколько лет вклад: ")
monthly_cap = (safe_input("int",True,"Ежемесячная капитализация процентов (1-да, остальное-нет)")==1)
for y in range(years):
    deposit = count_interest(deposit, interest_rate, monthly_cap)
    print(f"После {y+1} года депозит будет {deposit}")