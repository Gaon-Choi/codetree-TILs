elem = range(1, 10)

cnt = 0

N = int(input())

for i in range(N):
    for j in range(N):
        print(elem[cnt % 9], end="")
        cnt += 1
    print()