my_tuple = (
    "hello",
    3.14,
    [1, 2, 3],
    42,
    "world",
    [4, 5],
    [6, 7, 8, 9],
)

nested_list = []
for item in my_tuple:
  if isinstance(item, list):
    nested_list.append(item)

print("Original tuple:", my_tuple)
print("Nested list of lists:", nested_list)