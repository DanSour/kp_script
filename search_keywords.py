import requests
import config
import json

def film_json(film_name):
    # Замените {id} на нужный вам идентификатор фильма
    # film_id = '910353'  # Пример идентификатора
    # url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{film_id}'
    film = ''
    url = f'https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword={film_name}'

    # Заголовки запроса
    headers = {
        'X-API-KEY': config.api_key,
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(url, headers=headers)

        # Проверяем, успешен ли запрос
        if response.status_code == 200:
            film_data = response.json()  # Преобразуем ответ в JSON
            film_data = film_data['films'][0]
            # print(film_data)  # Выводим данные о фильме
            # with open('data_keywords_api.json', 'w', encoding='utf-8') as f:
                # json.dump(film_data, f, ensure_ascii=False, indent=4)
            return film_data

        else:
            print(f'Ошибка: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
