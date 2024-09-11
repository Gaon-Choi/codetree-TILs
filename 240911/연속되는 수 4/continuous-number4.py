N = int(input())

arr = []

counts = []

for _ in range(N):
    elem = int(input())
    if len(arr) == 0 or arr[-1] < elem:
        arr.append(elem)
    else:
        counts.append(len(arr))
        arr = [elem]

if len(counts) == 0:
    print(1)
else:
    print(max(counts))