import copy

N, B = map(int, input().split())

presents = []

for _ in range(N):
    presents.append(int(input()))

results = []

for i in range(len(presents)):
    temp_present = copy.deepcopy(presents)
    temp_present[i] = temp_present[i] // 2
    temp_present.sort()

    total_budget = 0
    
    for k in range(len(temp_present)):
        if total_budget + temp_present[k] > B:
            results.append(k)
            break
        else:
            total_budget += temp_present[k]

print(max(results))