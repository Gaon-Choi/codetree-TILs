N, M = map(int, input().split())

a = 0
b = 0

a_move = []
b_move = []

for _ in range(N):
    speed, hour = map(int, input().split())

    for __ in range(hour):
        a += speed
        a_move.append(a)

for _ in range(M):
    speed, hour = map(int, input().split())

    for __ in range(hour):
        b += speed
        b_move.append(b)

result = 0

arr = []

for i in range(len(a_move)):
    if (a_move[i] - b_move[i]) != 0:
        arr.append(a_move[i] - b_move[i])

for i in range(len(arr) - 1):
    if arr[i] * arr[i+1] < 0:
        result += 1

print(result)