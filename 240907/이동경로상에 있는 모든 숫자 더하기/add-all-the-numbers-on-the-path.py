dx = [-1, 0, +1, 0]
dy = [0, +1, 0, -1]

offset = 0

N, T = map(int, input().split())
queries = list(input())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

x = (N-1) // 2
y = (N-1) // 2

result = matrix[x][y]

for q in queries:
    if q == "F":
        if 0 <= x + dx[offset % 4] and x + dx[offset % 4] < N and 0 <= y + dy[offset % 4] and y + dy[offset % 4] < N:
            x += dx[offset % 4]
            y += dy[offset % 4]
            result += matrix[x][y]
    elif q == "R":
        offset += 1
    elif q == "L":
        offset -= 1
    else:
        continue

print(result)