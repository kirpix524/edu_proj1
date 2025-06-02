import requests
import pprint

def main():
    # URL API GitHub для поиска репозиториев
    url = 'https://api.github.com/search/repositories'

    # Параметр q=html — поиск репозиториев, где встречается "html"
    params = {'q': 'html'}

    # Отправляем GET-запрос
    response = requests.get(url, params=params)

    # Печатаем код статуса
    print(f'Код статуса: {response.status_code}')

    # Печатаем содержимое ответа в формате JSON
    try:
        data = response.json()
        print('JSON-ответ:')
        pprint.pprint(data)
    except ValueError:
        print('Ошибка: не удалось декодировать ответ как JSON')


if __name__ == '__main__':
    main()