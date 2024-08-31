def calculate_sum(N: int):
    if N == 0:
        return 0
    else:
        return N + calculate_sum(N - 1)

N = int(input())
print(calculate_sum(N))