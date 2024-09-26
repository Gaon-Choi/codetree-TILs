def is_comfortable_zone(i, j, N, matrix):
    cnt = 0

    if (0 <= i-1 and i-1 < N) and (0 <= j and j < N):
        if matrix[i-1][j] == 1:
            cnt += 1

    if (0 <= i+1 and i+1 < N) and (0 <= j and j < N):
        if matrix[i+1][j] == 1:
            cnt += 1

    if (0 <= i and i < N) and (0 <= j-1 and j-1 < N):
        if matrix[i][j-1] == 1:
            cnt += 1

    if (0 <= i and i < N) and (0 <= j+1 and j+1 < N):
        if matrix[i][j+1] == 1:
            cnt += 1

    return True if cnt == 3 else False

N, M = map(int, input().split())

matrix = [[0] * N for _ in range(N)]

answers = []

for _ in range(M):
    r, c = map(int, input().split())
    r -= 1; c -= 1

    matrix[r][c] = 1

    answers.append(1 if is_comfortable_zone(r, c, N, matrix) else 0)

for elem in answers:
    print(elem)