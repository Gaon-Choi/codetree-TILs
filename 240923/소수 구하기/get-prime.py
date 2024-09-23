def is_prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())

for num in range(1, n + 1):
    if is_prime(num):
        print(num, end=" ")