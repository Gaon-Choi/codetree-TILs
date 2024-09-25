def is_reachable(x, y, N):
    if 0 <= x and x < N and 0 <= y and y < N:
        return True
    return False

def find_direction(temp_dirr):
    for idx, value in enumerate(temp_dirr):
        if value != -1:
            return idx

direction = [[-1, 0], [+1, 0], [0, +1], [0, -1]]

n, r, c = map(int, input().split())
r -= 1; c -= 1

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

while True:
    print(matrix[r][c], end=" ")

    temp = []

    temp.append(matrix[r-1][c] if is_reachable(r-1,c,n) and matrix[r-1][c] > matrix[r][c] else -1)
    temp.append(matrix[r+1][c] if is_reachable(r+1,c,n) and matrix[r+1][c] > matrix[r][c] else -1)
    temp.append(matrix[r][c+1] if is_reachable(r,c+1,n) and matrix[r][c+1] > matrix[r][c] else -1)
    temp.append(matrix[r][c-1] if is_reachable(r,c-1,n) and matrix[r][c-1] > matrix[r][c] else -1)

    if max(temp) == -1:
        break

    dirr = find_direction(temp)
    r += direction[dirr][0]
    c += direction[dirr][1]