arr = []

for _ in range(10):
    elem = int(input())

    if 0 <= elem and elem <= 200:
        arr.append(elem)

print(sum(arr), format(round(sum(arr) / len(arr), 1), ".1f"))