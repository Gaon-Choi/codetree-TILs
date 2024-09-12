N = int(input())

cnt = 0

while(True):
    if N >= 1000:
        break

    if N % 2 == 0:
        N = 3 * N + 1
    else:
        N = 2 * N + 2

    cnt += 1

print(cnt)