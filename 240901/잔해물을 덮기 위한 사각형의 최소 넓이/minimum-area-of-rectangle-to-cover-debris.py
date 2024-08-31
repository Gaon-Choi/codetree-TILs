size = 2001
offset = size // 2

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())

matrix = [[0] * size for _ in range(size)]

for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        matrix[i + offset][j + offset] = 1

for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        matrix[i + offset][j + offset] = 0

x_points = []
y_points = []

for i in range(size):
    for j in range(size):
        if matrix[i][j] == 1:
            x_points.append(i)
            y_points.append(j)

if not x_points:
    print(0)
elif not y_points:
    print(0)
else:
    print((max(x_points) - min(x_points) + 1) * (max(y_points) - min(y_points) + 1))