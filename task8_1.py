import random

n = 10
arr = [random.randint(1, 12) for _ in range(n)]
print("Original array:", arr)

power = 1
for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = 10**power
        power += 1

print("Array after modifying even indices:", arr)

if len(arr) > 2:
    arr.pop(0)
    arr.pop()
    print("Resulting array after removing first and last elements:", arr)
else:
    print("The array is too short to remove elements.")