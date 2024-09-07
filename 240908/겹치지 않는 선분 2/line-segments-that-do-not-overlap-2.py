size = 1000000

N = int(input())


offset = size

points = []

for _ in range(N):
    points.append(list(map(int, input().split())))

result = 0

for i in range(N):
    for j in range(N):
        arr = [0] * (2 * size + 1)

        if i != j:
            for k in range(points[j][0], points[j][1]):
                arr[k + offset] = 1

    is_intersect = False

    for m in range(points[i][0], points[i][1]):
        if arr[m + offset] == 1:
            is_intersect = True
            break
    
    if not is_intersect:
        result += 1
        
print(result)