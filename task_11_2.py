import json

with open("years.json", "r", encoding="utf-8") as f:
    years = json.load(f)

with open("prices.json", "r", encoding="utf-8") as f:
    prices = json.load(f)

newest_year = max(years.values())
print(f"Найновіші телефони ({newest_year} рік):")
for model, year in years.items():
    if year == newest_year:
        print(f"  {model}, ціна: {prices.get(model, 'невідома')}")

cheapest = sorted(prices.items(), key=lambda item: item[1])[:3]
print("Найдешевші моделі:")
for model, price in cheapest:
    print(f"  {model}: {price}, рік випуску: {years.get(model, 'невідомий')}")