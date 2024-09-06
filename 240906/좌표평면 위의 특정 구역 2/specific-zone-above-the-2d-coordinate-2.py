import copy

N = int(input())

x = []
y = []

for _ in range(N):
    x_, y_ = map(int, input().split())
    x.append(x_)
    y.append(y_)

temp = []

for i in range(N):
    temp_x = copy.deepcopy(x)
    temp_y = copy.deepcopy(y)

    temp_x.pop(i)
    temp_y.pop(i)

    temp.append((max(temp_x) - min(temp_x)) * (max(temp_y) - min(temp_y)))

print(min(temp))