size = 201
offset = size // 2

matrix = [[0] * size for _ in range(size)]

N = int(input())

for v in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    # red : 1, blue : 2
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i + offset][j + offset] = (v % 2) + 1

result = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] == 2:
            result += 1

print(result)