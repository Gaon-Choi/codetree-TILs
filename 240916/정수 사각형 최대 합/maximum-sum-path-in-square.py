n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

matrix = [[0] * n for _ in range(n)]

# 아랫 줄
matrix[0][0] = arr[0][0]

for i in range(1, n):
    matrix[i][0] = matrix[i-1][0] + arr[i][0]
    #matrix[i][i] = matrix[i-1][i-1] + arr[i][i]

for i in range(n):
    for j in range(i + 1):
        if matrix[i][j] == 0:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) + arr[i][j]

# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=" ")
#     print()

print(matrix[n - 1][n - 1])