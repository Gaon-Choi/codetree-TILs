n = int(input())

dx = [0, -1, 0, +1]
dy = [+1, 0, -1, 0]

matrix = [[0] * n for _ in range(n)]

x = n // 2
y = n // 2

offset = 0
size = 1
rround = 0
colored = 1

matrix[x][y] = colored
colored += 1

while(colored <= n ** 2):
    for _ in range(size):
        x += dx[offset % 4]
        y += dy[offset % 4]
        if 0<=x and x<n and 0<=y and y<n:
            matrix[x][y] = colored
            colored += 1

    offset += 1
    rround += 1

    if rround % 2 == 0:
        size += 1
    
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()