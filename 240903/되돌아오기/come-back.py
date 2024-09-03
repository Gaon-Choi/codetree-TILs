dx = {
    "N": 0,
    "E": +1,
    "S": 0,
    "W": -1
}

dy = {
    "N": +1,
    "E": 0,
    "S": -1,
    "W": 0
}

N = int(input())

queries = []
for _ in range(N):
    q = input().split()
    queries.extend([q[0]] * int(q[1]))

loc = [0, 0]
count = 0
reach = False

for q in queries:
    loc[0] += dx[q]
    loc[1] += dy[q]
    count += 1

    if loc[0] == 0 and loc[1] == 0:
        reach = True
        break

if reach:
    print(count)
else:
    print(-1)