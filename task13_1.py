class COMP:
    def __init__(self, model, inv_number, price):
        self.model = model
        self.inv_number = inv_number
        self.price = price

    def __del__(self):
        print("Об'єкт видалено:", self.model, self.inv_number)

    def change_inv_number(self, new_inv_number):
        self.inv_number = new_inv_number

    def change_price(self, new_price):
        self.price = new_price

    def show(self):
        print(f"Модель: {self.model}, інв. номер: {self.inv_number}, ціна: {self.price}")


def show_all(computers):
    for i, comp in enumerate(computers, 1):
        print(i, end=") ")
        comp.show()


def sort_by_price(computers):
    computers.sort(key=lambda c: c.price)


def find_by_model(computers, model):
    return [c for c in computers if c.model.lower() == model.lower()]


def total_price(computers):
    return sum(c.price for c in computers)


def choose_comp(computers):
    index = int(input("Введіть номер комп'ютера (1-9): ")) - 1
    if 0 <= index < len(computers):
        return computers[index]
    print("Невірний номер")
    return None


def main():
    computers = [
        COMP("Dell Inspiron", 1001, 25000),
        COMP("HP Pavilion", 1002, 22000),
        COMP("Lenovo ThinkPad", 1003, 35000),
        COMP("Asus VivoBook", 1004, 20000),
        COMP("Acer Aspire", 1005, 18000),
        COMP("MSI Modern", 1006, 27000),
        COMP("Apple MacBook", 1007, 55000),
        COMP("Huawei MateBook", 1008, 30000),
        COMP("Samsung Galaxy Book", 1009, 28000),
    ]

    while True:
        print()
        print("1 - Показати всі комп'ютери")
        print("2 - Сортувати за ціною")
        print("3 - Знайти за моделлю")
        print("4 - Загальна вартість")
        print("5 - Показати один комп'ютер")
        print("6 - Змінити інвентарний номер")
        print("7 - Змінити ціну")
        print("0 - Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all(computers)
        elif choice == "2":
            sort_by_price(computers)
            show_all(computers)
        elif choice == "3":
            found = find_by_model(computers, input("Модель: "))
            if found:
                show_all(found)
            else:
                print("Нічого не знайдено")
        elif choice == "4":
            print("Загальна вартість:", total_price(computers))
        elif choice == "5":
            comp = choose_comp(computers)
            if comp:
                comp.show()
        elif choice == "6":
            comp = choose_comp(computers)
            if comp:
                comp.change_inv_number(int(input("Новий інвентарний номер: ")))
                comp.show()
        elif choice == "7":
            comp = choose_comp(computers)
            if comp:
                comp.change_price(float(input("Нова ціна: ")))
                comp.show()
        elif choice == "0":
            break
        else:
            print("Невірний вибір")


main()
