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

n, m, k = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

height = 0

while height + 1 < n:
    is_ = False
    for i in range(k-1, k+m-1):
        if matrix[height + 1][i] == 1:
            is_ = True
            break
    if is_:
        break
    height += 1

for i in range(k-1, k+m-1):
    matrix[height][i] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()