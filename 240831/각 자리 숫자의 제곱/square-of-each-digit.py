def digit_square_sum(N: int):
    if N < 10:
        return N**2
    else:
        return digit_square_sum(N // 10) + (N % 10) ** 2

n = int(input())
print(digit_square_sum(n))