# импорт используемых библиотек
from imdb import IMDb
import csv
import os

ia = IMDb()
file_path_imdb = "C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv"

# Проверка наличия файла для записи результата
if (not os.path.exists(file_path_imdb)) or os.path.getsize(file_path_imdb) == 0:
    # Открыть файл на запись, тем самым создав его
    with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv", "w", encoding="utf-8",newline='') as file:
        a_pen = csv.writer(file)
        # Записать названия столбцов
        a_pen.writerow(('imdb_id', 'oscar_win_count', 'oscar_nominee_count', 'other_win_count', 'other_nominee_count', 'imdb_budget',' Worldwide_Gross', 'producer_list', 'writer_list', 'companies_list', 'isTopRated'))

with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/detailed_kp.csv", "r", encoding="utf-8",newline='') as input_file, open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv", "a", encoding="utf-8",newline='') as output_file:
    reader = csv.reader(input_file) # Считать файл целиком
    writer = csv.writer(output_file)
    count = 0
    for i in reader:  # Проход в цикле по каждому элементу
        count += 1
        if count == 1: # Пропустить строку с названиями признаков
            continue

        # Проверить, что у фильма есть идентификатор на сервисе "IMDb"
        if i[1] != '':
            movie_info = ia.get_movie(i[1][2:]) # Выполнить запрос
            # Поиск всей информации
            try:
                top250 = movie_info['top 250 rank']
            except:
                top250 = None

            try:
                companies_list = []
                for z in movie_info['production companies']:
                    companies_list.append(z['name'])
            except:
                companies_list = None

            try:
                writer_list = []
                for z in movie_info['writers']:
                    writer_list.append(z['name'])
            except:
                writer_list = None

            try:
               imdb_budget = movie_info['box office']['Budget']
            except:
               imdb_budget = None

            try:
                Worldwide_Gross = movie_info['box office']['Cumulative Worldwide Gross']
            except:
                Worldwide_Gross = None

            try:
                producer_list = []
                for z in movie_info['producers']:
                    producer_list.append(z['name'])
            except:
                producer_list = None

            oscar_win_count = 0
            oscar_nominee_count = 0
            other_win_count = 0
            other_nominee_count = 0
            try:
                movie = ia.get_movie(i[ 1][2:], info=['awards'])
                rez = movie['awards']
                for j in rez:
                    if j['award'] == 'Oscar':
                        if j['result'] == 'Winner':
                            oscar_win_count += 1
                        else:
                            oscar_nominee_count += 1
                    else:
                        if j['result'] == 'Winner':
                            other_win_count += 1
                        else:
                            other_nominee_count += 1
            except:
                writer.writerow((i[1], oscar_win_count, oscar_nominee_count, other_win_count, other_nominee_count, imdb_budget, Worldwide_Gross, producer_list, writer_list, companies_list, top250))
        else:
            writer.writerow(('No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info', 'No IMDB info'))
