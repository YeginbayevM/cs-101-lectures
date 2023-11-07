# Подсчёт favorites с помощью переменных

import csv

# Открытие CSV-файла
with open("favorites.csv", "r") as file:

    # Инициализация DictReader
    reader = csv.DictReader(file)

    # Инициализация счётчиков
    scratch, c, python = 0, 0, 0

    # Итерация по CSV-файлу с подсчётом favorites
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

# Вывод подсчитанного количества scratch, c и python
print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
