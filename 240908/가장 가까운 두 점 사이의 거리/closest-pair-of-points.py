def calculate_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

N = int(input())

points = []
results = []

for _ in range(N):
    points.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        results.append(calculate_distance(points[i][0], points[i][1], points[j][0], points[j][1]))

print(min(results))