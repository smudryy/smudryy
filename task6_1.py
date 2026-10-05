import math

a = float(input("Enter range start a: "))
b = float(input("Enter range end b: "))
h = float(input("Enter step h: "))

print("1. Loop with parameter")
steps = round((b - a) / h) + 1
for i in range(steps):
  x = a + i * h
  fx = math.cos(x) / (1 + abs(math.sin(x)))
  print(f"x = {x:.4f}, f(x) = {fx:.4f}")

print("2. Loop with precondition")
x = a
while x <= b:
  fx = math.cos(x) / (1 + abs(math.sin(x)))
  print(f"x = {x:.4f}, f(x) = {fx:.4f}")
  x += h

print("3. Lists and element search")
values = []
x = a
while x <= b:
  fx = math.cos(x) / (1 + abs(math.sin(x)))
  values.append(fx)
  x += h

print("All function values in a column:")
for val in values:
  print(f"{val:.4f}")

if values:
  max_val = max(values)
  min_val = min(values)

  max_idx = values.index(max_val)
  min_idx = values.index(min_val)

  start_idx = min(max_idx, min_idx)
  end_idx = max(max_idx, min_idx)

  sub_list = values[start_idx + 1 : end_idx]

  print(f"Maximum value: {max_val:.4f} (index {max_idx})")
  print(f"Minimum value: {min_val:.4f} (index {min_idx})")
  print("Elements between maximum and minimum:")
  if sub_list:
    for val in sub_list:
      print(f"{val:.4f}")
  else:
    print("There are no other elements between them.")
else:
  print("The list is empty")