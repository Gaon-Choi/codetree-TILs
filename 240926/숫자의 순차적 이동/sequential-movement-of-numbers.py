dirr = [[-1, 0], [-1, +1], [0, +1], [+1, +1], [+1, 0], [+1, -1], [0, -1], [-1, -1]]

def change_with_max(i, j, N, matrix):
    temp = []
    for d in dirr:
        if 0 <= i + d[0] and i + d[0] < N and 0 <= j + d[1] and j + d[1] < N:
            temp.append(matrix[i + d[0]][j + d[1]])
        else:
            temp.append(-1)

    maxIdx = temp.index(max(temp))

    matrix[i][j], matrix[i + dirr[maxIdx][0]][j + dirr[maxIdx][1]] = matrix[i + dirr[maxIdx][0]][j + dirr[maxIdx][1]], matrix[i][j]

def find_out_n(n, N, matrix):
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == n:
                return [x, y]

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for _ in range(m):
    for num in range(1, n ** 2 + 1):
        X, Y = find_out_n(num, n, matrix)

        change_with_max(X, Y, n, matrix)

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()