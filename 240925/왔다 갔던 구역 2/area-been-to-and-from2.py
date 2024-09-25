walk = dict()

curr = 0

N = int(input())

for _ in range(N):
    dist, direction = input().split()
    dist = int(dist)

    direction = +1 if direction == "R" else -1

    for _ in range(dist):
        now_ = curr
        next_ = curr + direction

        if next_ < now_:
            now_, next_ = next_, now_

        key = "{a} {b}".format(a=now_, b=next_)
        curr += direction

        if key in walk:
            walk[key] += 1
        else:
            walk[key] = 1

print(len(list(filter(lambda x : x >= 2, walk.values()))))