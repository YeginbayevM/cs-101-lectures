# Подсчёт понравившихся задач заместо языков программирования

import csv

# Открытие CSV-файла
with open("favorites.csv", "r") as file:

    # Инициализация DictReader
    reader = csv.DictReader(file)

    # Инициализация счётчика
    counts = {}

    # Итерация по CSV-файлу с подсчётом понравившихся задач
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Вывод подсчитанного количества задач
for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")
