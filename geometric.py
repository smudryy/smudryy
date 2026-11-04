def geometric_sum(b1, q, n):
    if q == 1:
        return b1 * n
    return b1 * (q ** n - 1) / (q - 1)


def geometric_nth(b1, q, n):
    return b1 * q ** (n - 1)
