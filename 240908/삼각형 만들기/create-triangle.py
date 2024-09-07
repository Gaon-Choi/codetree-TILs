def is_perpendicular(p1, p2, p3):
    s1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    s2 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
    s3 = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2

    set1 = set([p1[0], p2[0], p3[0]])
    set2 = set([p1[1], p2[1], p3[1]])

    if (s3 == s1 + s2) or (s1 == s2 + s3) or (s2 == s1 + s3):
        if len(set1) == 2 and len(set2) == 2:
            return True
        else:
            return False
    else:
        return False

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
            if is_perpendicular(points[i], points[j], points[k]):
                results.append(calculate_area(points[i], points[j], points[k]))

print(max(results))