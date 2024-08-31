def digit_sum(N: int):
    if N < 10:
        return N
    else:
        return (N % 10) + digit_sum(N // 10)

a, b, c = map(int, input().split())

print(digit_sum(a * b * c))