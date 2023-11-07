# Вывод всех данных из favorites в формате CSV с помощью csv.reader

import csv

# Открытие CSV-файла
with open("favorites.csv", "r") as file:

    # Объявление переменной reader
    reader = csv.reader(file)

    # Пропуск первой строки (заголовки столбцов)
    next(reader)

    # Итерация по CSV-файлу с выводом каждой записи из favorite
    for row in reader:
        print(row[1])
