n = int(input())

arr = [[0] * n for _ in range(n)]

for j in range(n):
    if j % 2 == 1:
        for i in range(j + 1):
            arr[i][j] = 1
    else:
        arr[0][j] = 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()