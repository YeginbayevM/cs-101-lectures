# Сортировка favorites по ключу

import csv

# Открытие CSV-файла
with open("favorites.csv", "r") as file:

    # Инициализация DictReader
    reader = csv.DictReader(file)

    # Инициализация счётчика
    counts = {}

    # Итерация по CSV-файлу с подсчётом favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Вывод подсчитанного количества scratch, c и python
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
