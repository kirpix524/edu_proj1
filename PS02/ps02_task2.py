import requests


def main():
    # URL API с поддержкой фильтрации по URL-параметрам
    url = 'https://jsonplaceholder.typicode.com/posts'

    # Фильтруем записи по полю userId=1
    params = {'userId': 1}

    # Отправляем GET-запрос
    response = requests.get(url, params=params)

    # Печатаем код статуса
    print(f'Код статуса: {response.status_code}\n')

    # Печатаем полученные записи
    try:
        posts = response.json()
        print('Записи пользователя с userId=1:')
        for post in posts:
            print(f"\nID: {post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Тело: {post['body']}")
    except ValueError:
        print('Ошибка: не удалось декодировать ответ как JSON')


if __name__ == '__main__':
    main()
