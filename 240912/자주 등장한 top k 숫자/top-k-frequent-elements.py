n, k = map(int, input().split())

element = dict()

arr = list(map(int, input().split()))

for elem in arr:
    if elem in element:
        element[elem] += 1
    else:
        element[elem] = 1

results = []

for e in element:
    results.append([element[e], e])

results.sort(key = lambda x: (-x[0], -x[1]))


for i in range(k):
    print(results[i][1], end=" ")