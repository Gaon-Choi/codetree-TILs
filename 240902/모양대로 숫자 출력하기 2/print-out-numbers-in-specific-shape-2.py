elem = range(2, 10, 2)

cnt = 0

N = int(input())

for i in range(N):
    for j in range(N):
        print(elem[cnt % len(elem)], end=" ")
        cnt += 1
    print()