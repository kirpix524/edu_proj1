import requests


def main():
    # URL API для создания новых записей
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Данные, которые отправляем в POST-запросе
    payload = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    # Отправляем POST-запрос с JSON-данными
    response = requests.post(url, json=payload)

    # Печатаем код статуса
    print(f'Код статуса: {response.status_code}')

    # Печатаем содержимое ответа
    try:
        data = response.json()
        print('Ответ JSON:')
        print(data)
    except ValueError:
        print('Ошибка: не удалось декодировать ответ как JSON')


if __name__ == '__main__':
    main()
