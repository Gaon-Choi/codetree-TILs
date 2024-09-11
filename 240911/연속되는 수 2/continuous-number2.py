prev = -1

N = int(input())

count = 0

arr = []
results = []

for _ in range(N):
    a = int(input())

    if len(arr) == 0 or arr[-1] == a:
        arr.append(a)
    else:
        results.append(len(arr))
        arr = [a]

if len(arr) > 0:
    results.append(len(arr))

print(max(results))