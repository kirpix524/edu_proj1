import time
import csv
import re
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import numpy as np
import matplotlib.pyplot as plt

# Отключаем уведомления (если необходимо)
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.divan.ru/category/divany")

# Ждём, чтобы первоначальные карточки загрузились
time.sleep(3)

def get_card_count():
    return len(driver.find_elements(By.CSS_SELECTOR, "div._Ud0k"))

parsed_data = []
prev_count = get_card_count()

# Скроллим до подгрузки всех карточек
while True:
    try:
        pagination = driver.find_element(By.CSS_SELECTOR, "div.ui-jDl24")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", pagination)
        time.sleep(2)
        new_count = get_card_count()
        if new_count > prev_count:
            prev_count = new_count
            continue
        else:
            break
    except Exception as e:
        print("Пагинация недоступна или всё подгружено:", e)
        break

# Сбор данных
cards = driver.find_elements(By.CSS_SELECTOR, "div._Ud0k")
for card in cards:
    try:
        name = card.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text.strip()
    except:
        name = ""
    try:
        price_text = card.find_element(By.CSS_SELECTOR, "span.KIkOH[data-testid='price']").text.strip()
        # Преобразуем текст цены в число, убирая всё лишнее
        price = float(re.sub(r"[^\d.,]", "", price_text).replace(",", "."))
    except:
        price = np.nan
    try:
        href = card.find_element(By.CSS_SELECTOR, "a.ProductName").get_attribute("href")
        detail_url = href if href.startswith("http") else urljoin(driver.current_url, href)
    except:
        detail_url = ""
    parsed_data.append([name, price, detail_url])

driver.quit()

# Записываем результат в CSV
csv_filename = "divan_sofas_all_pages.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "price", "detail_url"])
    writer.writerows(parsed_data)

# Извлекаем цены в numpy-массив, отбрасывая NaN
prices = np.array([row[1] for row in parsed_data], dtype=float)
prices = prices[~np.isnan(prices)]

# Вычисляем и выводим среднюю цену
average_price = prices.mean()
print(f"Средняя цена дивана: {average_price:.2f} руб.")

# Строим гистограмму цен
plt.figure(figsize=(8, 5))
plt.hist(prices, bins=30)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

print(f"Готово! Всего записано товаров: {len(parsed_data)}. Файл: {csv_filename}")
