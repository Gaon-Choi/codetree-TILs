def is_propagatable(list_1, list_2):
    for i in range(len(list_1)):
        if list_1[i] == list_2[i]:
            return True
    return False

def blow_from_left(row):
    return [row[-1]] + row[0:-1]

def blow_from_right(row):
    return row[1:] + [row[0]]

N, M, Q = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))


location, direction = input().split()
location = int(location) - 1

up = location - 1
down = location + 1

curr_direction = 1 if direction == "R" else 0

if curr_direction == 1:
    arr[location] = blow_from_right(arr[location])
else:
    arr[location] = blow_from_left(arr[location])

up_ = curr_direction
down_ = curr_direction

while up >= 0:
    up_ += 1
    if is_propagatable(arr[up], arr[up+1]):
        if up_ % 2 == 1:
            arr[up] = blow_from_right(arr[up])
        else:
            arr[up] = blow_from_left(arr[up])
        up -= 1
    else:
        break

while down < N:
    down_ += 1
    if is_propagatable(arr[down], arr[down-1]):
        if down_ % 2 == 1:
            arr[down] = blow_from_right(arr[down])
        else:
            arr[down] = blow_from_left(arr[down])
        down += 1
    else:
        break
    
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()