r = 0; c = 0

dx = [0, +1, 0, -1]
dy = [-1, 0, +1, 0]

offset = 0

queries = list(input())

for t, q in enumerate(queries):
    if q == "F":
        r += dx[offset % 4]
        c += dy[offset % 4]

        if r == 0 and c == 0:
            print(t + 1)
            exit(0)

    elif q == "R":
        offset += 1
    else:
        offset -= 1

print(-1)