# Kinopoisk_data_processing
## Сбор, обработка и подготовка данных о фильмах, предоставляемых сервисами "Кинопоиск" и "IMDb", для прогнозирования вероятностых оценок
### Идея: 
В одном CSV файле собрать датасет, состоящих из всех фильмов, представленных на Кинопоиске, и признаков: жанры, год выхода, оценки на Кинопоиске, IMDb, Metacritic, количество оценок, хронометраж, актеры, режиссерский состав, наличие в ТОП250, временная категория, наличие премии "Оскар".
### Реализация:
Структура проекта:
1. Сбор данных (Requests, BeautifulSoup)
2. Обработка данных (Pandas)

Сбор данных:
 - Признаки фильмов: API (requests)
 - Оценки, которые выставил пользователь: API не предоставляет данную информацию (на момент создания программы такого функционала не было). Она есть в открытом доступе на официальном сайте Кинопоиска. Подходит парсинг (Requests, BeautifulSoup)

Обработка данных:
 - Анализ признаков, добавление новых + удаление тех, где количество пропусков > 50%
 - Нормализация данных
 - Бинаризация категориальных признаков (MultiLabelBinarizer)
 - Заполнение пропусков по KNN

Результат:
 - Обработанный набор данных - для обучения моделей машинного обучения: задача регрессии и кластеризации
 - Необработанный набор данных - для визуализации