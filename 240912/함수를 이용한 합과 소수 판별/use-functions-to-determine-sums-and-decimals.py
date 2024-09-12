def is_prime_and_digit_sum_even(n: int):
    # 소수 여부 판별
    for i in range(2, n):
        if n % i == 0:
            return False

    if sum(list(map(int, list(str(n))))) % 2 == 0:
        return True
    return False

a, b = map(int, input().split())

cnt = 0

for i in range(a, b + 1):
    if is_prime_and_digit_sum_even(i):
        cnt += 1

print(cnt)