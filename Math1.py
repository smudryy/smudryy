import math

x = float(input("Enter a number x: "))

numeration = math.cos(x) + math.log(abs(x) + 1)
denominator = math.exp(0.7 * x) + math.pow(4, 3.3 * x + 1)

if x >= 0:
    second_term = 0.9 * math.pow(x, math.sqrt(2 * x))
    f_x = (numeration / denominator) - second_term
    print("The value of the function f(x) is:", f_x)
else:
    raise ValueError("x must be non-negative for the second term calculation.")

