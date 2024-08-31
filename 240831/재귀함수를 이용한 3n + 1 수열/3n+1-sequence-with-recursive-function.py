def when_3n_1(N):
    if N == 1:
        return 0
    else:
        if N % 2 == 0:
            return 1 + when_3n_1(N // 2)
        else:
            return 1 + when_3n_1(3 * N + 1)

N = int(input())
print(when_3n_1(N))