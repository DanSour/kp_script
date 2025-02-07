from config import *
from search_keywords import film_json
import pandas as pd


def get_movie_type(movie_vars):
    genres = set(movie_vars.get('genres', '').lower().split(', '))
    movie_type = movie_vars.get('type', '')

    # Определение типа произведения на основе жанров и типа
    if 'аниме' in genres:
        if movie_type in ['TV_SERIES', 'MINI_SERIES']:
            return 'Аниме-сериал'
        elif movie_type == 'FILM':
            return 'Мульт'
    elif 'мультфильм' in genres:
        if movie_type in ['TV_SERIES', 'MINI_SERIES']:
            return 'Мульт-сериал'
        elif movie_type == 'FILM':
            return 'Мульт'
    
    # Определение типа произведения по типу (если жанры не помогли)
    type_mapping = {
        'FILM': 'Фильм',
        'TV_SERIES': 'Сериал',
        'MINI_SERIES': 'Сериал'
    }
    
    return type_mapping.get(movie_type, 'Неизвестный тип')

def main():
    movie = input('Фильм или сериал: ')
    mov_vars = film_json(movie)
    if mov_vars == None:
        return
        
    keys_to_keep = ["nameRu", "posterUrl", "year", "genres", "rating", "filmLength", "type"]
    mov_vars = {k: v for k, v in mov_vars.items() if k in keys_to_keep} 

    mov_vars['genres'] = ', '.join([item['genre'] for item in mov_vars['genres']])
    mov_vars['posterUrl'] = f'<img src={mov_vars["posterUrl"]} alt="img" width="100" />'
    
    mov_vars['type'] = get_movie_type(mov_vars)
    
    mov_data = pd.DataFrame([mov_vars], columns=keys_to_keep)
    mov_data = mov_data.to_markdown(index=False)
    mov_data = mov_data.split('\n')[2:]
    mov_data = mov_data[0]
    
    with open(movies_table, 'a', encoding='utf-8') as file:
        file.write(mov_data + '\n')
        file.close


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
