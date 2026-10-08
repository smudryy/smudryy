s = input("Enter a string with at least two digits: ")

first_digit_idx = -1
last_digit_idx = -1

for i, char in enumerate(s):
  if char.isdigit():
    if first_digit_idx == -1:
      first_digit_idx = i 
    last_digit_idx = i  

if first_digit_idx != -1 and last_digit_idx != -1 and first_digit_idx != last_digit_idx:
  result = s[: first_digit_idx + 1] + s[last_digit_idx:]
  print("Resulting string:", result)
else:
  print("Error: The string must contain at least two digits.")
