n = int(input())

arr = [[0] * n for _ in range(n)]
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 0

for i in range(n):
    for j in range(i, n):
        arr[i][j] = digits[num % 9]
        num += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            print(" ", end=" ")
        else:
            print(arr[i][j], end=" ")
    print()