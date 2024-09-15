n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        arr[i][j] = n-j

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            print(" ", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()