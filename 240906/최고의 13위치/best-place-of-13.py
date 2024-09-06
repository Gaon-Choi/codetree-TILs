N = int(input())

block_i = 1
block_j = 3

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

max_sum = -1

for i in range(N - block_i + 1):
    for j in range(N - block_j + 1):
        max_sum = max(max_sum, arr[i][j] + arr[i][j + 1] + arr[i][j + 2])

print(max_sum)