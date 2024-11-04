import math

n, k = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sum_matrix = [[0] * n for _ in range(n)]
sum_matrix[0][0] = matrix[0][0]

for i in range(1, n):
    sum_matrix[0][i] = sum_matrix[0][i-1] + matrix[0][i]
    sum_matrix[i][0] = sum_matrix[i-1][0] + matrix[i][0]

for i in range(1, n):
    for j in range(1, n):
        sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1] + matrix[i][j]

result = -math.inf

for i in range(n - k + 1):
    for j in range(n - k + 1):
        result = max(result, sum_matrix[i+k-1][j+k-1] - sum_matrix[i][j])

print(result)