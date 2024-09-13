points = dict()

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if x in points:
        points[x].append(y)
    else:
        points[x] = [y]

answer = 0

for elem in points:
    answer += min(points[elem])

print(answer)