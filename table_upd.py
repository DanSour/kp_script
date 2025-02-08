from config import *
from data_preparation import *
import pandas as pd
from search_keywords import film_json


def main():
    movie = input('Фильм или сериал: ')
    mov_vars = film_json(movie)
    if mov_vars == None:
        return
    
    mov_data = movie_preparation(mov_vars)
    with open(movies_table, 'a', encoding='utf-8') as file:
        file.write(mov_data + '\n')
        file.close


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
