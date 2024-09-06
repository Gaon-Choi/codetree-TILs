n = int(input())

arr = list(map(int, input().split()))

max_mult = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            max_mult = max(max_mult, arr[i] * arr[j] * arr[k])

print(max_mult)