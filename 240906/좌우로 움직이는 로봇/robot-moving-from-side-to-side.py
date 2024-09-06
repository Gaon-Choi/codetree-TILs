a = 0
b = 0

n, m = map(int, input().split())

a_move = []
b_move = []

for _ in range(n):
    dist, direction = input().split()
    dist = int(dist)

    if direction == "R":
        for __ in range(dist):
            a += 1
            a_move.append(a)
    else:
        for __ in range(dist):
            a -= 1
            a_move.append(a)

for _ in range(m):
    dist, direction = input().split()
    dist = int(dist)

    if direction == "R":
        for __ in range(dist):
            b += 1
            b_move.append(b)
    else:
        for __ in range(dist):
            b -= 1
            b_move.append(b)

size_offset = len(a_move) - len(b_move)

if size_offset > 0:
    b_move.extend([b_move[-1]] * size_offset)
elif size_offset < 0:
    a_move.extend([a_move[-1]] * abs(size_offset))

result = 0

for i in range(len(a_move) - 1):
    if a_move[i+1] == b_move[i+1] and a_move[i] != b_move[i]:
        result += 1

print(result)