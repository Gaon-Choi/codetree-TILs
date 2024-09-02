elem = range(9, 0, -1)

N = int(input())

cnt = 0

for i in range(N):
    for j in range(N):
        print(elem[cnt % len(elem)], end="")
        cnt += 1
    print()