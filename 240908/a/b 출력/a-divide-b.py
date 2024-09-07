a, b = map(int, input().split())

result = []

result.append(a // b)

for _ in range(20):
    result.append(str((a * 10) // b))
    a = a // b

print("{integer}.{sosu}".format(integer=result[0], sosu=''.join(result[1:])))