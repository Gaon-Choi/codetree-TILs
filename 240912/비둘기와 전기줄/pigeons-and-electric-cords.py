bidulgi = [[] for _ in range(10 + 1)]

N = int(input())

for _ in range(N):
    bidul, loc = map(int, input().split())
    bidulgi[bidul].append(loc)

result = 0

for i in range(1, 11):
    cnt = 0

    if len(bidulgi[i]) == 1:
        continue

    for j in range(len(bidulgi[i])-1):
        if bidulgi[i][j] != bidulgi[i][j+1]:
            cnt += 1
    result += cnt

print(result)