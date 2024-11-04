n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

answer = 0

for i in range(n - 1):
    for j in range(n - 1):
        answer = max(answer, matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1])
        answer = max(answer, matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1])
        answer = max(answer, matrix[i][j]+matrix[i][j+1]+matrix[i+1][j])
        answer = max(answer, matrix[i][j]+matrix[i][j+1]+matrix[i+1][j+1])

for i in range(n):
    for j in range(n - 2):
        answer = max(answer, matrix[i][j]+matrix[i][j+1]+matrix[i][j+2])

for i in range(n - 2):
    for j in range(n):
        answer = max(answer, matrix[i][j]+matrix[i+1][j]+matrix[i+2][j])

print(answer)