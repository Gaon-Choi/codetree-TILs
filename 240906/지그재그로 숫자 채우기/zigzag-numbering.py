cnt = 0

n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1

    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()