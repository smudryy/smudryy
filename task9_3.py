import random


heights = {
    "Іваненко": 165,
    "Петренко": 172,
    "Коваленко": 158,
    "Шевченко": 180,
    "Бондаренко": 169,
    "Ткаченко": 175,
    "Мельник": 162,
    "Кравченко": 170,
    "Олійник": 177,
    "Лисенко": 160
}

ages = {surname: random.randint(14, 17) for surname in heights}

print("Зріст:", heights)
print("Вік:  ", ages)