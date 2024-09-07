def check_location(x: int, y: int, size: int, arr):
    if x >= 0 and x < size and y >= 0 and y < size:
        if arr[i][j] == 1:
            return 1
        else:
            return 0
    else:
        return 0

N = int(input())

matrix = []
result = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        count = check_location(i-1, j, N, matrix) + check_location(i+1, j, N, matrix) + check_location(i, j-1, N, matrix) + check_location(i, j+1, N, matrix)

        if count == 3:
            result += 1

print(result)