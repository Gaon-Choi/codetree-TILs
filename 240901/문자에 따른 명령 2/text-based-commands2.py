offset = 0

# N, E, S, W
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]

queries = input()

loc = [0, 0]

for query in queries:
    if query == "L":
        offset -= 1
    elif query == "R":
        offset += 1
    elif query == "F":
        loc[0] += dx[offset % 4]
        loc[1] += dy[offset % 4]

print(loc[0], loc[1])