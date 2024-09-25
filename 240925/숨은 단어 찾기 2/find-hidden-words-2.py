def is_reachable(x, y, n, m):
    if 0 <= x and x < n and 0 <= y and y < m:
        return True
    return False

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(input()))

cnt = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == "L":
            if is_reachable(i, j+1, N, M) and is_reachable(i, j+2, N, M) and matrix[i][j+1] =="E" and matrix[i][j+2] == "E":
                cnt += 1
            if is_reachable(i+1, j+1, N, M) and is_reachable(i+2, j+2, N, M) and matrix[i+1][j+1] =="E" and matrix[i+2][j+2] == "E":
                cnt += 1
            if is_reachable(i+1, j, N, M) and is_reachable(i+2, j, N, M) and matrix[i+1][j] =="E" and matrix[i+2][j] == "E":
                cnt += 1
            if is_reachable(i+1, j-1, N, M) and is_reachable(i+2, j-2, N, M) and matrix[i+1][j-1] =="E" and matrix[i+2][j-2] == "E":
                cnt += 1
            if is_reachable(i, j-1, N, M) and is_reachable(i, j-2, N, M) and matrix[i][j-1] =="E" and matrix[i][j-2] == "E":
                cnt += 1
            if is_reachable(i-1, j-1, N, M) and is_reachable(i-2, j-2, N, M) and matrix[i-1][j-1] =="E" and matrix[i-2][j-2] == "E":
                cnt += 1
            if is_reachable(i-1, j, N, M) and is_reachable(i-2, j, N, M) and matrix[i-1][j] =="E" and matrix[i-2][j] == "E":
                cnt += 1
            if is_reachable(i-1, j+1, N, M) and is_reachable(i-2, j+2, N, M) and matrix[i-1][j+1] =="E" and matrix[i-2][j+2] == "E":
                cnt += 1

print(cnt)