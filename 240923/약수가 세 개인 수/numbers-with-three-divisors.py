def is_divisor_three(n: int):
    cnt = 0

    for i in range(2, n):
        if n % i == 0:
            cnt += 1

    return True if cnt == 1 else False

total_number = 0

start, end = map(int, input().split())

for i in range(start, end + 1):
    if is_divisor_three(i):
        total_number += 1

print(total_number)