# Используемые библиотеки
import requests
import os
import csv

file_path_detailed = "C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/detailed_kp.csv"
token = 'HQGPD9P-HZ24JY1-KXZ4PCC-0E9YPD1'

# Проверка наличия файла для записи
if (not os.path.exists(file_path_detailed)) or os.path.getsize(file_path_detailed) == 0:
    # Открыть файл на зпись, тем самым создав его
    with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/detailed_kp.csv", "w", encoding="utf-8",newline='') as file:
        # Записать названия признаков
        a_pen = csv.writer(file)
        a_pen.writerow(("KP_id", "imdb_id", "genres", "actors","directors", "countries", "budget", "budget_currency", "WorldwideGross", "WorldwideGross_currency", "backdrop"))

with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/correct_all_data_3.csv", "r", encoding="utf-8",newline='') as input_file, open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/detailed_kp.csv", "a", encoding="utf-8",newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    count = 0
    for j in reader: # цикл для построчного считывания CSV-файла результата работы программы 1
        count += 1
        if count == 1: # Игнорировать строку с названиями столбцов
            continue
        # Выполнить запрос по идентификатору фильма
        response = requests.get(f"https://api.kinopoisk.dev/movie?search={j[0]}&field=id&token=HQGPD9P-HZ24JY1-KXZ4PCC-0E9YPD1")
        data = response.json() # Преобразовать ответ из JSON объекта в словарь для поиска значений нужных признаков
        try:
            # Проверка выполнения запроса
            if data['message'] == "You made more than 5000 requests per day. The limits will be updated at 00: 00. To get more limits and a personal token, write to telegram @mdwit":
                break
        except:
            print('Продолжаем')
        # Зафиксировать значения всех новых признаков. Если признак у фильма отсуствует, то записать None
        try:
            imdb_id = data["externalId"]["imdb"]
        except:
            imdb_id = None
        try:
            persons_list = []
            extended_actors_list = []
            extended_directors_list = []
            # Формирование списков всех актерови режиссеров
            for i in data['persons']:
                persons_list.append({i["id"]:i['name']})
                if i['enProfession'] == "actor":
                    extended_actors_list.append(i["name"])
                if i["enProfession"] == "director":
                    extended_directors_list.append(i["name"])

        except:
            persons_list = None
            extended_actors_list = None
            extended_directors_list = None
        try:
            trailer = data['videos']['trailers'][0]['url']
        except:
            trailer = None

        try:
            budget = data['budget']['value']
        except:
            budget = None

        try:
            budget_currency = data['budget']['currency']
        except:
            budget_currency = None

        try:
            world_fees = data['fees']['world']['value']
        except:
            world_fees = None

        try:
            world_fees_currency = data['fees']['world']['currency']
        except:
            world_fees_currency = None

        try:
            genres_list = []
            for i in data['genres']:
                genres_list.append(i['name'])
        except:
            genres_list = None

        try:
            countries_list = []
            for i in data['countries']:
                countries_list.append(i['name'])
        except:
            countries_list = None

        try:
            backdrop = data['backdrop']['url']
        except:
            backdrop = None
        # Запись результатов в CSV-файл
        writer.writerow((j[0],imdb_id,genres_list,extended_actors_list,extended_directors_list,countries_list,budget,budget_currency,world_fees,world_fees_currency,backdrop))
