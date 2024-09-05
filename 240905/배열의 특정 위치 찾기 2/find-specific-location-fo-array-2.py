even = 0
odd = 0

arr = list(map(int, input().split()))

for i in range(len(arr)):
    if i % 2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

print(abs(even - odd))