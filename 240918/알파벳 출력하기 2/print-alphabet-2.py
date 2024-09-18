N = int(input())

alphabet = range(65, 65 + 26)

idx = 0

cnt = 0

for i in range(N):
    for j in range(N):
        if j < cnt:
            print(" ", end=" ")
        else:
            print(chr(alphabet[idx % 26]), end=" ")
            idx += 1
    cnt += 1
    print()