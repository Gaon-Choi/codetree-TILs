n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(0, n):
            arr[j][i] = j + 1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = n - j

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()