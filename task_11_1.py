import csv

authors = []

# Количество писателей: 10-15
n = 0
while not 10 <= n <= 15:
    n = int(input("Скільки письменників введете (10-15)? "))

for i in range(n):
    surname = input(f"Прізвище письменника {i + 1}: ")
    year = int(input(f"Рік народження ({surname}): "))
    authors.append((surname, year))

# Сортировка по году рождения по возрастанию
authors.sort(key=lambda a: a[1])

# Запись в CSV
with open("authors.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Прізвище", "Рік народження"])
    writer.writerows(authors)

print("Дані записано у authors.csv")