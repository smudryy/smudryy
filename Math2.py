import math

x = float(input("Enter a number x: "))
y = float(input("Enter a number y: "))
z = float(input("Enter a number z: "))

under_root = 0.7 * math.cos(x) + math.log(abs(y))

if(under_root < 0):
    term1 = -math.pow(abs(under_root), 1/5)
else:
    term1 = math.pow(under_root, 1/5)

term2 = math.exp(z + x)

R = term1 + term2

print("The value of the function R is:", R)