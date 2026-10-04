import math

a = float(input("Enter bar side a: "))
b = float(input("Enter bar side b: "))
c = float(input("Enter bar length c: "))

m = float(input("Enter width m: "))
n = float(input("Enter height n: "))

block_sides = sorted([a, b])
hole_sides = sorted([m, n])

if block_sides[0] <= hole_sides[0] and block_sides[1] <= hole_sides[1]:
    print("The block can pass through the hole.")
else:
    print("The block cannot pass through the hole.")