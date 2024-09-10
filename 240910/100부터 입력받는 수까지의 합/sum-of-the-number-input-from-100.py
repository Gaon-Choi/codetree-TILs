def sum_to_n(n: int):
    return n * (n + 1) // 2


n = int(input())

print(sum_to_n(100) - sum_to_n(n - 1))