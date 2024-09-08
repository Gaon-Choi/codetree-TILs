cnt = 1

n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            arr[i][j] = cnt
            cnt += 1
    else:
        for j in range(n-1, -1, -1):
            arr[i][j] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()