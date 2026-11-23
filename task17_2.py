import pandas as pd

with open("data.txt", encoding="utf-8") as file:
    values = file.read().replace(",", ".").split()
temperature = pd.Series([float(value) for value in values])

with open("obrobka.txt", "w", encoding="utf-8") as file:
    file.write(f"Найменше значення: {temperature.min()}\n")
    file.write(f"Найбільше значення: {temperature.max()}\n")
    file.write(f"Середнє значення: {temperature.mean():.2f}\n")
    file.write(f"Медіана: {temperature.median()}\n")
print(open("obrobka.txt", encoding="utf-8").read())
