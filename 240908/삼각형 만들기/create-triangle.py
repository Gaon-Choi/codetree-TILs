def calculate_area(p1, p2, p3):
    return (max(p1[0], p2[0], p3[0]) - min(p1[0], p2[0], p3[0])) * (max(p1[1], p2[1], p3[1]) - min(p1[1], p2[1], p3[1]))

n = int(input())

points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

results = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            results.append(calculate_area(points[i], points[j], points[k]))

print(max(results))