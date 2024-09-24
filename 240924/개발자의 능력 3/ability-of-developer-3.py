import math

arr = list(map(int, input().split()))

min_difference = math.inf

for i in range(6):
    for j in range(i, 6):
        for k in range(j, 6):
            sum_1 = arr[i] + arr[j] + arr[k]
            sum_2 = sum(arr) - sum_1
            min_difference = min(min_difference, abs(sum_1 - sum_2))

print(min_difference)