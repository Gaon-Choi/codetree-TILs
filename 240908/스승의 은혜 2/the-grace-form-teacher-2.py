N, B = map(int, input().split())

presents = []

for _ in range(N):
    presents.append(int(input()))

presents.sort()

results = []

for i in range(len(presents)):
    total_budget = 0
    for k in range(len(presents)):
        d_budget = (presents[k] // 2) if k == i else presents[k]
        if total_budget + d_budget > B:
            results.append(k)
            break
        else:
            total_budget += d_budget

print(max(results))