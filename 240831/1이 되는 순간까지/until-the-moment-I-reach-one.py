def until_become_one(N:int):
    if N == 1:
        return 0
    else:
        if N % 2 == 0:
            return 1 + until_become_one(N // 2)
        else:
            return 1 + until_become_one(N // 3)

N = int(input())
print(until_become_one(N))