import random

N = 4

matrix = [[random.randint(1, 35) for _ in range(N)] for _ in range(N)]

print("Matrix:")
for row in matrix:
    print(row)

sum_above = 0
sum_below = 0

for i in range(N):
    for j in range(N):
        if i < j:  
            sum_above += matrix[i][j]
        elif i > j:  
            sum_below += matrix[i][j]

print(f"Sum of elements above the main diagonal: {sum_above}")
print(f"Sum of elements below the main diagonal: {sum_below}")
