# E -> S -> W -> N
dx = [+1, 0, -1, 0]
dy = [0, +1, 0, -1]

offset = 0

m, n = map(int, input().split())

matrix = [[0] * n for _ in range(m)]

idx = 0
size = m * n

loc = [0, 0]

for idx in range(size):
    matrix[loc[1]][loc[0]] = chr(65 + idx % 26)
    idx += 1
    if not (0 <= loc[0] + dx[offset % 4] and loc[0] + dx[offset % 4] < n and 0 <= loc[1] + dy[offset % 4] and loc[1] + dy[offset % 4] < m and matrix[loc[1] + dy[offset % 4]][loc[0] + dx[offset % 4]] == 0):
        offset += 1
    loc[0] += dx[offset % 4]
    loc[1] += dy[offset % 4]

for row in matrix:
    for elem in row:
        print(elem, end = " ")
    print()