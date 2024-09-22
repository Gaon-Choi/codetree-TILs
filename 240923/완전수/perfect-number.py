def is_perfect_number(n: int):
    total_divisor = 0
    for i in range(1, n):
        if n % i == 0:
            total_divisor += i
    
    return True if n == total_divisor else False

start, end = map(int, input().split())

num = 0

for i in range(start, end + 1):
    if is_perfect_number(i):
        num += 1

print(num)