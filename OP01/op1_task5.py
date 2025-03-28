import requests

def get_exchange_rate(date):
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = requests.get(url)
    if response.status_code == 200:
        from xml.etree import ElementTree as ET
        tree = ET.fromstring(response.content)
        for valute in tree.findall(".//Valute"):
            char_code = valute.find("CharCode").text
            if char_code == "USD":
                return float(valute.find("Value").text.replace(",", "."))
    print("Ошибка получения курса валют")
    return None

def currency_converter():
    date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    try:
        amount = float(input("Введите сумму в долларах: "))
        exchange_rate = get_exchange_rate(date)
        if exchange_rate:
            result = amount * exchange_rate
            print(f"Сумма в рублях на {date}: {result:.2f} RUB")
        else:
            print("Не удалось получить курс доллара на указанную дату.")
    except ValueError:
        print("Ошибка: введите корректную сумму!")

if __name__ == "__main__":
    currency_converter()
