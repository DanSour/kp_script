from kinopoisk.movie import Movie
from config import *
import traceback
import json
import pandas as pd
from search_keywords import film_json

def mov_processing(line):
    if line.startswith('- '):
        movie = line[2:].strip() # читаем с третьего символа и удаляем пробелы с концов
        if movie == '':
            return
        if '(' in movie:
            movie = movie.split('(')[0].strip()

        movie = movie.lower() # переводим в нижний регистр
        try:
            # result = Movie.objects.search(movie)
            film_data = film_json(movie)

        except Exception as e:
            # print('фильм не найден')
            # print()
            with open(movies_table, 'a', encoding='utf-8') as file:
                file.write(f'| {movie} | -- | -- | -- | -- | -- |' + '\n')
                file.close

            return
        # mov_vars = vars(film_data)
        mov_vars = film_data

        keys_to_keep = ["nameRu", "posterUrl", "year", "genres", "rating", "filmLength"]
        mov_vars = {k: v for k, v in mov_vars.items() if k in keys_to_keep} 

        # mov_vars['genres'] = [genre['genre'] for genre in mov_vars['genres']]
        mov_vars['genres'] = mov_vars['genres'].apply(lambda x: ', '.join([item['genre'] for item in x]))

        # try:
        mov_vars['posterUrl'] = f'<img src={mov_vars["posterUrl"]} alt="img" width="100" />'
        # except Exception as e:
            # pass
        
        mov_data = pd.DataFrame([mov_vars], columns=keys_to_keep)
        mov_data = mov_data.to_markdown(index=False)
        mov_data = mov_data.split('\n')[2:]
        mov_data = mov_data[0]
        
        with open(movies_table, 'a', encoding='utf-8') as file:
            file.write(mov_data + '\n')
            file.close

    return


def main():
    with open(movies_table, 'w', encoding='utf-8') as file:
        file.write('| nameRu | year | filmLength | genres | rating | posterUrl | ' + '\n' + 
                   '| -- | -- | -- | -- | -- | -- |' + '\n')
        file.close

    with open(movies_file, 'r', encoding='utf-8') as file:
        for line in file:
            mov_processing(line)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()