import random

NAMES = [
    "Олександр", "Марія", "Іван", "Софія", "Андрій", "Анна",
    "Дмитро", "Олена", "Максим", "Катерина", "Богдан", "Наталія",
]


def generate_line(names, max_length=100):
    limit = random.randint(1, max_length)
    line = ""
    while True:
        name = random.choice(names)
        candidate = name if not line else line + " " + name
        if len(candidate) > limit:
            break
        line = candidate
    if not line:
        line = random.choice(names)[:limit]
    return line


def main():
    n = int(input("Введіть кількість рядків N: "))
    with open("output.txt", "w", encoding="utf-8") as file:
        for _ in range(n):
            file.write(generate_line(NAMES) + "\n")
    print("Записано рядків:", n)


main()
