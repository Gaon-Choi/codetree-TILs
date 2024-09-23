n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n -1:
            arr[i][j] = 1

for i in range(1, n):
    for j in range(i):
        arr[i][j] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()