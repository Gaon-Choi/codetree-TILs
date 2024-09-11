def is_perfect_number(n: int):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += if
    
    if total == n:
        return True
    return False

N = int(input())

if is_perfect_number(N):
    print("P")
else:
    print("N")