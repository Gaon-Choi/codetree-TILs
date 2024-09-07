direction = {
    "L": [0, -1],
    "R": [0, +1],
    "U": [-1, 0],
    "D": [+1, 0]
}

n, t = map(int, input().split())

# r행 c열
r, c, d = input().split()
r = int(r); c = int(c)

for _ in range(t):
    if  (1 <= r + direction[d][0]) and (r + direction[d][0] <= n) and  (1 <= c + direction[d][1]) and (c + direction[d][1] <= n):
        r += direction[d][0]
        c += direction[d][1]
    else:
        if d == "L":
            d = "R"
        elif d == "R":
            d = "L"
        elif d == "U":
            d = "D"
        else:
            d = "U"

print(r, c)