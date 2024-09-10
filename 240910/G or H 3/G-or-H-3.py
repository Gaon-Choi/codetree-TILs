N, K = map(int, input().split())

max_size = 10000

arr = [0] * (max_size + 1)

for _ in range(N):
    loc, alphabet = input().split()
    loc = int(loc)

    if alphabet == "G":
        arr[loc] = 1
    else:
        arr[loc] = 2

results = []

for i in range(max_size - K + 1):
    results.append(sum(arr[i:i+K+1]))

print(max(results))