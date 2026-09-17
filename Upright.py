width = float(input("Enter the width of the upright: "))
height = float(input("Enter the height of the upright: "))
k = float(input("Enter the proportionality coefficient: "))

new_width = width * k
new_height = height * k


print("Size of the upright after scaling:")
print("Width:", new_width)
print("Height:", new_height)