n = int(input())

arr = [[0] * n for _ in range(n)]

num = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            num += 1
        else:
            num += 2
        arr[i][j] = num

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()