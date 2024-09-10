n, k = map(int, input().split())

arr = list(map(int, input().split()))

max_val = 0

for i in range(n - k + 1):
    max_val = max(sum(arr[i:i+k]), max_val)

print(max_val)