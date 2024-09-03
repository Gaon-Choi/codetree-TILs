def strange_series(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return strange_series(n // 3) + strange_series(n - 1)

n = int(input())
print(strange_series(n))