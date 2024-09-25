walk = dict()

curr = 0

N = int(input())

for _ in range(N):
    dist, direction = input().split()
    dist = int(dist)

    direction = +1 if direction == "R" else -1

    for _ in range(dist):
        curr += direction
        if curr in walk:
            walk[curr] += 1
        else:
            walk[curr] = 1

print(len(list(filter(lambda x : x >= 2, walk.values()))))