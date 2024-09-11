total = 0

n = int(input())

for _ in range(n):
    total += int(input())

print(total, format(round(total / n, 1), ".1f"))