# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
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

deposit = float(input("Сумма, которую вы хотите положить на счет: "))
interest_rate = float(input("Процентная ставка, годовых: "))
years = int(input("На сколько лет вклад: "))
monthly_cap = (int(input("Ежемесячная капитализация процентов (1-да, 0-нет)"))==1)
for y in range(years):
    deposit = count_interest(deposit, interest_rate, monthly_cap)
    print(f"После {y+1} года депозит будет {deposit}")


