size = 201
offset = size // 2

matrix = [[0] * size for _ in range(size)]

N = int(input())

query = []

for _ in range(N):
    query.append(list(map(int, input().split())))

for q in query:
    for i in range(q[0] + offset, q[2] + offset):
        for j in range(q[1] + offset, q[3] + offset):
            matrix[i][j] = 1

print(sum(sum(row) for row in matrix))