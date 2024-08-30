n, m = map(int, input().split())

gcd = 1
for i in range(1, min(n, m)):
    if n % i == 0 and m % i == 0:
        gcd = i

print(gcd)