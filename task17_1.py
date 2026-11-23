import pandas as pd

df = pd.read_csv("driver.csv", encoding="utf-8")
disciplines = ["Будова автомобіля", "Правила дорожнього руху", "Водіння автомобіля"]

surname = input("Введіть прізвище студента: ")
print(df.loc[df["Прізвище"] == surname, disciplines].to_string(index=False))

df[df["Спроби"] == 1].to_csv("proba.csv", index=False, encoding="utf-8-sig")
print("Відомості записано у proba.csv")
