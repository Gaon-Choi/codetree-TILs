dirs = [[-1, +1], [-1, -1], [+1, -1], [+1, +1]]


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

r, c, m1, m2, m3, m4, direction = map(int, input().split())

r -= 1
c -= 1

location_arr = []
value_arr = []

for _ in range(m1):
    r += dirs[0][0]
    c += dirs[0][1]
    location_arr.append([r, c])
    value_arr.append(matrix[r][c])
    

for _ in range(m2):
    r += dirs[1][0]
    c += dirs[1][1]
    location_arr.append([r, c])
    value_arr.append(matrix[r][c])
    

for _ in range(m3):
    r += dirs[2][0]
    c += dirs[2][1]
    location_arr.append([r, c])
    value_arr.append(matrix[r][c])
    

for _ in range(m4):
    r += dirs[3][0]
    c += dirs[3][1]
    location_arr.append([r, c])
    value_arr.append(matrix[r][c])

if direction == 0:
    value_arr = [value_arr[-1]] + value_arr[0:len(value_arr) - 1]
else:
    value_arr = value_arr[1:] + [value_arr[0]]

i = 0
for point in location_arr:
    x, y = point[0], point[1]
    matrix[x][y] = value_arr[i]
    i += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()