n, m = map(int, input().split())

# n : 격자의 크기
# m : 동전의 개수

arr = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()