size = 201
offset = size // 2

matrix = [[0] * size for _ in range(size)]

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a + offset, a + 8 + offset):
        for j in range(b + offset, b + 8 + offset):
            matrix[i][j] = 1

print(sum(sum(row) for row in matrix))