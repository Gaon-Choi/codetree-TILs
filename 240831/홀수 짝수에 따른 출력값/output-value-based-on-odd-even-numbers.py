def even_odd_sum(N: int):
    # initial condition
    if N == 1:
        return 1
    if N == 2:
        return 2
    
    return N + even_odd_sum(N - 2)

n = int(input())
print(even_odd_sum(n))