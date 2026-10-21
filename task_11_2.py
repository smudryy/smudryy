import ast

# Чтение словарей из текстовых файлов
with open("years.txt", "r", encoding="utf-8") as f:
    years = ast.literal_eval(f.read())

with open("prices.txt", "r", encoding="utf-8") as f:
    prices = ast.literal_eval(f.read())

# 1) Самые новые телефоны (может быть несколько с одним годом)
newest_year = max(years.values())
print(f"Найновіші телефони ({newest_year} рік):")
for model, year in years.items():
    if year == newest_year:
        print(f"  {model}, ціна: {prices.get(model, 'невідома')}")

# 2) Три самые дешёвые модели
cheapest = sorted(prices.items(), key=lambda item: item[1])[:3]
print("Найдешевші моделі:")
for model, price in cheapest:
    print(f"  {model}: {price}, рік випуску: {years.get(model, 'невідомий')}")