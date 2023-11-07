# Вывод всех данных из favorites в формате CSV с помощью csv.DictReader

import csv

# Открытие CSV-файла
with open("favorites.csv", "r") as file:

    # Инициализация DictReader
    reader = csv.DictReader(file)

    # Итерация по CSV-файлу с выводом каждой записи из favorite
    for row in reader:
        print(row["language"])
