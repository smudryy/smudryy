import geometric

def main():
    b1 = float(input("Введіть перший член b1: "))
    q = float(input("Введіть знаменник q: "))
    n = int(input("Введіть N: "))
    print("Сума перших", n, "членів:", geometric.geometric_sum(b1, q, n))
    print(n, "-й член:", geometric.geometric_nth(b1, q, n))


main()
