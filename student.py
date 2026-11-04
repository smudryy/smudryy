class STUDENT:
    def __init__(self, name, sname, year, marks):
        self.Name = name
        self.SName = sname
        self.Year = year
        self.Marks = list(marks)
        self.AverMark = 0
        self.CalcAvMark()

    def CalcAvMark(self):
        if self.Marks:
            self.AverMark = sum(self.Marks) / len(self.Marks)
        else:
            self.AverMark = 0
        return self.AverMark

    def DisplayAll(self):
        print(f"Ім'я: {self.Name}")
        print(f"Прізвище: {self.SName}")
        print(f"Рік народження: {self.Year}")
        print(f"Оцінки: {self.Marks}")
        print(f"Середня оцінка: {self.AverMark:.2f}")
        print()
