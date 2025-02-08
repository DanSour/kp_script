from config import *
from search_keywords import film_json
from data_preparation import *


def main():
    movies_table_v2 = f'{movies_table[:-3]}_v2.md'
    with open(movies_table_v2, 'w', encoding='utf-8') as file:
        file.write('| Название | img | Год | Жанры | Рейтинг | Длительность | Тип |' + '\n')
        file.write('| - | - | - | - | - | - | - |' + '\n')
        file.close

    with open(movies_table, 'r', encoding='utf-8') as file:
        next(file)  # Пропускаем первую строку
        next(file)  # Пропускаем вторую строку
        for line in file:
            movie = line.split("|")[1:]
            name = movie[0]
            poster = movie[1]
            year = movie[2]
            format = movie[6]
            if not format.startswith('  ') :
                with open(movies_table_v2, 'a', encoding='utf-8') as file:
                    file.write(line)
                    file.close
                    continue
            mov_vars = film_json(f'{name} {year}')
            if mov_vars == None:
                with open(movies_table_v2, 'a', encoding='utf-8') as file:
                    file.write(line)
                    file.close
                    continue

            mov_data = movie_preparation(mov_vars)
            mov_data_split = mov_data.split("|")[1:]
            if mov_data_split[1].split(' ')[2] == poster.split(' ')[2]:
                print(mov_data)
                with open(movies_table_v2, 'a', encoding='utf-8') as file:
                    file.write(mov_data + '\n')
                    file.close
                    continue
            
            with open(movies_table_v2, 'a', encoding='utf-8') as file:
                file.write(line)
                file.close

        file.close
    return


if __name__ == '__main__':
    main()