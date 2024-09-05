arr = list(map(int, input().split()))

idx = arr.index(0)

print(arr[idx - 3] + arr[idx - 2] + arr[idx - 1])