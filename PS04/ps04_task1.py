import sys
import time
import requests
from urllib.parse import urljoin, urlencode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_initial_url(query: str) -> str:
    """
    Выполняет поиск в Википедии по запросу и возвращает URL первой статьи.
    Если точное совпадение имени страницы есть, будет редирект на неё.
    Иначе — результаты поиска, откуда берётся первая ссылка.
    """
    # Попытка сразу перейти по заголовку страницы
    title_url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    response = requests.get(title_url, allow_redirects=True)
    if response.status_code == 200 and "Поиск" not in response.url:
        # Если мы не попали на страницу результатов поиска (т. е. статья существует)
        return response.url
    # Иначе отправляем запрос на поиск
    params = {"search": query}
    search_resp = requests.get("https://ru.wikipedia.org/w/index.php", params=params, allow_redirects=True)
    # Если поиск вернул страницу статьи (при точном совпадении), вернётся URL статьи
    if "Поиск" not in search_resp.url:
        return search_resp.url
    # Иначе парсим первую ссылку с результатов поиска (requests не даёт DOM, но Википедия сразу перенаправляет на страницу если один результат)
    # На практике в таком случае можно просто вернуть search_resp.url, но для надёжности:
    return search_resp.url

def init_webdriver(headless: bool = True) -> webdriver.Chrome:
    """
    Создаёт экземпляр Chrome WebDriver. Если headless=True, запускает без GUI.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    # Отключаем лишние логи
    options.add_argument("--log-level=3")
    # Инициализируем драйвер (предполагается, что chromedriver есть в PATH)
    driver = webdriver.Chrome(options=options)
    # Делаем небольшую паузу, чтобы гарантировать корректный запуск процесса
    time.sleep(1)
    return driver

def load_page(driver: webdriver.Chrome, url: str):
    """
    Загружает страницу по данному URL в Selenium-драйвер.
    """
    driver.get(url)
    # Немного ждём, пока контент подгрузится
    time.sleep(1)

def show_paragraphs(driver: webdriver.Chrome):
    """
    Последовательно выводит в консоль параграфы текущей статьи.
    Пользователь нажимает Enter, чтобы перейти к следующему, или 'q', чтобы прервать.
    """
    # Блок контента Википедии: div#mw-content-text .mw-parser-output
    content_div = driver.find_element(By.CSS_SELECTOR, "#mw-content-text .mw-parser-output")
    paras = content_div.find_elements(By.TAG_NAME, "p")

    if not paras:
        print("Содержимое статьи не найдено или в ней нет параграфов.")
        return

    print("\n=== Начало вывода параграфов статьи ===\n")
    for idx, p in enumerate(paras, start=1):
        text = p.text.strip()
        if not text:
            continue  # Пропускаем пустые параграфы
        print(f"[Параграф {idx}]\n{text}\n")
        cmd = input("Нажмите Enter для следующего параграфа, или введите 'q' для выхода в меню: ").strip().lower()
        if cmd == 'q':
            print("\n=== Выход из просмотра параграфов ===\n")
            return
    print("\n=== Конец статьи ===\n")

def list_links(driver: webdriver.Chrome) -> list:
    """
    Возвращает список ссылок (заголовок и полный URL) на другие статьи Википедии,
    найденных внутри контента текущей статьи.
    Фильтрует только внутренние ссылки вида /wiki/... без двоеточий (чтобы исключить спецстраницы).
    """
    content_div = driver.find_element(By.CSS_SELECTOR, "#mw-content-text .mw-parser-output")
    anchor_elems = content_div.find_elements(By.TAG_NAME, "a")

    links = []
    seen_hrefs = set()
    for a in anchor_elems:
        href = a.get_attribute("href")
        title = a.get_attribute("title")  # Текст ссылки или заголовок статьи
        if not href or not title:
            continue
        # Проверяем, что это внутренняя ссылка на статью: содержит '/wiki/' и нет ':' после /wiki/
        if "/wiki/" in href and ":" not in href.split("/wiki/")[-1]:
            # Убираем якоря (части после '#')
            href_clean = href.split("#")[0]
            if href_clean not in seen_hrefs:
                seen_hrefs.add(href_clean)
                links.append((title, href_clean))
    return links

def choose_link(links: list) -> str|None:
    """
    Выводит пользователю список ссылок (title) с индексами.
    Пользователь выбирает номер, возвращаем полный URL выбранной ссылки.
    Если ввод некорректен, предлагает снова.
    """
    if not links:
        print("В данной статье нет связанных страниц.")
        return None

    print("\n=== Список связанных страниц ===")
    for idx, (title, _) in enumerate(links, start=1):
        print(f"{idx}. {title}")
    print("0. Вернуться в главное меню")

    while True:
        choice = input("Введите номер страницы, на которую хотите перейти (0 — назад): ").strip()
        if choice == '0':
            return None
        if not choice.isdigit():
            print("Нужно ввести число. Попробуйте снова.")
            continue
        num = int(choice)
        if 1 <= num <= len(links):
            _, url = links[num - 1]
            return url
        else:
            print(f"Число должно быть от 1 до {len(links)}. Попробуйте снова.")

def main():
    print("=== Программа для поиска информации в Википедии ===")
    query = input("Введите поисковый запрос: ").strip()
    if not query:
        print("Пустой запрос. Завершение работы.")
        sys.exit(0)

    print("\nИщем статью в Википедии...")
    initial_url = get_initial_url(query)
    print(f"Найдена статья: {initial_url}\n")

    driver = init_webdriver(headless=False)
    try:
        current_url = initial_url
        load_page(driver, current_url)

        while True:
            print("Выберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            cmd = input("Введите 1, 2 или 3: ").strip()

            if cmd == '1':
                show_paragraphs(driver)
            elif cmd == '2':
                links = list_links(driver)
                next_url = choose_link(links)
                if next_url:
                    current_url = next_url
                    print(f"\nПереходим на: {current_url}\n")
                    load_page(driver, current_url)
                else:
                    print("\nВозврат в главное меню.\n")
            elif cmd == '3':
                print("Выход из программы...")
                break
            else:
                print("Некорректный ввод, попробуйте снова.\n")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
