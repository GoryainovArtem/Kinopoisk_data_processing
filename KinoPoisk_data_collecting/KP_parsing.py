# Используемые библиотеки
import requests
import csv
import os

token = 'HQGPD9P-HZ24JY1-KXZ4PCC-0E9YPD1'
req_1 = 'https://api.kinopoisk.dev/movie?field=rating.kp&search=0-10&field=typeNumber&search=1&limit=50000&sortField=rating.kp&sortType=-1&token=HQGPD9P-HZ24JY1-KXZ4PCC-0E9YPD1'
path_kp = "C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data_3.csv"

# Проверка наличия файла для записи результата
if (not os.path.exists(path_kp)) or os.path.getsize(path_kp) == 0:
    # Создать CSV-файл, открыв его на запись
    with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data_3.csv", "w", encoding="utf-8",newline='') as file:
        # Добавить названия признаков
        a_pen = csv.writer(file)
        a_pen.writerow(("KP_id", "title", "title_alternative", "year", "poster", "rating_kinopoisk", "kinopoisk_votes", "imDbRating", "imDbRatingVotes", "CriticsVote", "Critics_votes_amount","description" , "runtimeMins"))
# Добавление информации в созданный файл
with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/all_data_3.csv", "a", encoding="utf-8",newline='') as file:
    a_pen = csv.writer(file)
    response = requests.get(req_1)     # Выполнить запрос
    data = response.json()["docs"]     # Конвертировать JSON объект в словарь
    for i in range(len(data)):         # Цикл по всем элементам полученного ответа
        # Поиск информации по каждому признаку. Если признак отсутствует, то записать None
        try:
            poster = data[i]['poster']['url']
        except:
            poster = None

        try:
            KpVote = data[i]['rating']['kp']
        except:
            KpVote = None

        try:
            ImdbVote = data[i]['rating']['imdb']
        except:
            ImdbVote = None

        try:
            CriticsVote = data[i]['rating']['filmCritics']
        except:
            CriticsVote = None

        try:
            KP_votes_amount  = data[i]['votes']['kp']
        except:
            KP_votes_amount = None

        try:
            imdb_votes_amount = data[i]['votes']['imdb']
        except:
            imdb_votes_amount = None

        try:
            Critics_votes_amount = data[i]['votes']['filmCritics']
        except:
            Critics_votes_amount = None

        try:
            Alernative_name = data[i]['alternativeName']
        except:
            Alernative_name = None

        try:
            Id = data[i]['id']
        except:
            Id = None

        try:
            Name = data[i]['name']
        except:
            Name = None

        try:
            description = data[i]['description']
        except:
            description = None

        try:
            year = data[i]['year']
        except:
            year = None

        try:
            movieLength = data[i]['movieLength']
        except:
            movieLength = None

        # Запись в CSV
        # KP_id", "title", "title_alternative", "year", "poster", "rating_kinopoisk", "kinopoisk_votes", "imDbRating", "imDbRatingVotes", "CriticsVote", "Critics_votes_amount","description" , "runtimeMins"))
        print(Id,Name,Alernative_name,year,poster,KpVote, KP_votes_amount,ImdbVote,imdb_votes_amount,CriticsVote,Critics_votes_amount,description,movieLength)
        a_pen.writerow((Id,Name,Alernative_name,year,poster,KpVote, KP_votes_amount,ImdbVote,imdb_votes_amount,CriticsVote,Critics_votes_amount,description,movieLength))
