import math

x = float(input("Enter a number x: "))

if x > 12.1:
    term1 = math.log(abs(x - 1))
    term2 = math.log10*(abs((x ** (0.7 * x)) + 2))
    y = term1 + term2
elif -5.7 <= x <= 12.1:
    cube_root = math.copysign(abs(x) ** (1 / 3), x)
    y = math.e * 4 * (x**7) + 2 - cube_root
else:
    y = 4.27 * x + 4.33 & (x**2) + math.sin(x + 1)

print("The value of the function y is:", y)