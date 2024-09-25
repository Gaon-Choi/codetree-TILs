def is_reachable(i, j, max_x, max_y):
    if 0 <= i and i < max_x and 0 <= j and j < max_y:
        return True
    return False

def get_average(x, y, matrix):
    total = matrix[x][y]
    cnt = 1

    if is_reachable(x-1, y, N, M):
        total += matrix[x-1][y]
        cnt += 1
    if is_reachable(x+1, y, N, M):
        total += matrix[x+1][y]
        cnt += 1
    if is_reachable(x, y-1, N, M):
        total += matrix[x][y-1]
        cnt += 1
    if is_reachable(x, y+1, N, M):
        total += matrix[x][y+1]
        cnt += 1

    return total // cnt

def rotate_edges_clockwise(r1, c1, r2, c2, matrix):
    point_arr = []
    value_arr = []

    for i in range(c1, c2 + 1):
        point_arr.append([r1, i])
        value_arr.append(matrix[r1][i])

    for i in range(r1+1, r2 + 1):
        point_arr.append([i, c2])
        value_arr.append(matrix[i][c2])

    for i in range(c2-1, c1, -1):
        point_arr.append([r2, i])
        value_arr.append(matrix[r2][i])

    for i in range(r2, r1, -1):
        point_arr.append([i, c1])
        value_arr.append(matrix[i][c1])

    value_arr = [value_arr[-1]] + value_arr[0:len(value_arr)-1]

    i = 0
    for point in point_arr:
        x, y = point[0], point[1]
        matrix[x][y] = value_arr[i]
        i += 1

def average_inner_side(r1, c1, r2, c2, matrix):
    temp_arr = []
    temp_val_arr = []

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            temp_arr.append([i, j])
            temp_val_arr.append(get_average(i, j, matrix))
    num = 0

    for point in temp_arr:
        x, y = point[0], point[1]
        matrix[x][y] = temp_val_arr[num]
        num += 1

N, M, Q = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1

    rotate_edges_clockwise(r1, c1, r2, c2, matrix)
    average_inner_side(r1, c1, r2, c2, matrix)

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()