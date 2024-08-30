def check_matrix(matrix, I, J):
    result = 0

    for i in range(I, I+3):
        for j in range(J, J+3):
            result += matrix[i][j]

    return result

matrix = []
maxima = -1

n = int(input())

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n - 2):
    for j in range(n - 2):
        if maxima < check_matrix(matrix, i, j):
            maxima = check_matrix(matrix, i, j)

print(maxima)