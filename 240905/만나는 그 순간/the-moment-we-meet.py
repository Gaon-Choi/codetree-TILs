import math

N, M = map(int, input().split())

a = []
b = []

curr_a = 0; curr_b = 0

for _ in range(N):
    direction, dist = input().split()
    dist = int(dist)

    if direction == "R":
        a.extend([+1] * dist)
    else:
        a.extend([-1] * dist)

for _ in range(M):
    direction, dist = input().split()
    dist = int(dist)

    if direction == "R":
        b.extend([+1] * dist)
    else:
        b.extend([-1] * dist)

period = math.lcm(len(a), len(b))

t = 0

for i in range(period):
    t += 1

    curr_a += a[i % len(a)]
    curr_b += b[i % len(b)]

    if curr_a == curr_b:
        print(t)
        break

if i == period - 1:
    print(-1)