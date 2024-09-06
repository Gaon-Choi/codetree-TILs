a, b = map(int, input().split())

remainder = [0] * b

while (a > 1):
    remainder[(a % b)] += 1
    a = (a // b)

result = 0

for v in remainder:
    result += v ** 2

print(result)