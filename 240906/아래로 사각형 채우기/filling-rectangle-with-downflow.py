N = int(input())

arr = [[0] * N for _ in range(N)]

cnt = 1

for i in range(N):
    for j in range(N):
        arr[j][i] = cnt
        cnt += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()