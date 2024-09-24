import math

arr = list(map(int, input().split()))
N = len(arr)

min_difference = math.inf

for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            sum_1 = arr[i] + arr[j] + arr[k]
            sum_2 = sum(arr) - sum_1
            min_difference = min(min_difference, abs(sum_1 - sum_2))

print(min_difference)