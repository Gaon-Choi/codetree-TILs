cnt = 1

N = int(input())

for i in range(N):
    for j in range(N):
        print(cnt, end=" ")
        cnt += 1
    print()