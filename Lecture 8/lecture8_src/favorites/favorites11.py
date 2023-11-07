# Поиск по базе данных по популярности задачи

import csv

from cs50 import SQL

# Открытие базы данных
db = SQL("sqlite:///favorites.db")

# Запрос пользователя на ввод понравившейся задачи (favorite)
favorite = input("Favorite: ")

# Поиск по введённому пользователу запросу
rows = db.execute("SELECT COUNT(*) FROM favorites WHERE problem LIKE ?", "%" + favorite + "%")

# Получение одной (и единственной) строки
row = rows[0]

# Вывод подсчитанного количества понравившейся задачи [COUNT(*)]
print(row["COUNT(*)"])
