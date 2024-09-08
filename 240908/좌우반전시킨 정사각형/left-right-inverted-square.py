n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = (i + 1) * (j + 1)

for i in range(n):
    for j in range(1, n + 1):
        print(arr[i][-j], end=" ")
    print()