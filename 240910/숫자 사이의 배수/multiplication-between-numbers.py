a, b = map(int, input().split())

arr = []

for elem in range(a, b + 1):
    if elem % 5 == 0 or elem % 7 == 0:
        arr.append(elem)

print(sum(arr), format(round(sum(arr) / len(arr), 1), ".1f"))