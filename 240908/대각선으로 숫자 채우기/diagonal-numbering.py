def is_valid(x, y, n, m):
    if 0 <= x and x < n and 0 <= y and y < m:
        return True
    else:
        return False

n, m = map(int, input().split())

cnt = 1

arr = [[0] * m for _ in range(n)]

location = []

for i in range(m):
    location.append([0, i])
for j in range(1, n):
    location.append([j, m-1])

cnt = 1

for l in location:
    x_, y_ = l
    arr[x_][y_] = cnt
    cnt += 1

    while(is_valid(x_+1, y_-1, n, m)):
        x_ += 1
        y_ -= 1
        arr[x_][y_] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")

    print()