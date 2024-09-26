def bubble_up(col, n, matrix):
    tmp = []
    cnt = 0
    
    for i in range(n):
        if matrix[i][col] == 0:
            cnt += 1
        else:
            tmp.append(matrix[i][col])

    for _ in range(cnt):
        tmp.insert(0, 0)

    for i in range(n):
        matrix[i][col] = tmp[i]

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

r, c = map(int, input().split())
r -= 1; c -= 1

bomb_size = matrix[r][c] - 1

for i in range(r - bomb_size, r + bomb_size + 1):
    if 0 <= i and i < n:
        matrix[i][c] = 0

for j in range(c - bomb_size, c + bomb_size + 1):
    if 0 <= j and j < n:
        matrix[r][j] = 0

for c in range(n):
    bubble_up(c, n, matrix)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()