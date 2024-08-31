def mult_100_mod(n: int) -> int:
    if n == 1:
        return 2
    if n == 2:
        return 4
    return (mult_100_mod(n - 1) * mult_100_mod(n - 2)) % 100

N = int(input())

print(mult_100_mod(N))