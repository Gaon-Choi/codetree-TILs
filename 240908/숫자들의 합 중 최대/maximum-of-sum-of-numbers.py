def digit_sum(n: int):
    return sum(list(map(int, str(n))))

x, y = map(int, input().split())

results = []

for i in range(x, y + 1):
    results.append(digit_sum(i))

print(max(results))