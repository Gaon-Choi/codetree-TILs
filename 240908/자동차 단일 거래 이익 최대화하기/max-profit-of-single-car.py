N = int(input())

arr = list(map(int, input().split()))

revenue = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        revenue.append(arr[j] - arr[i])

if len(revenue) > 0:
    print(max(revenue))
else:
    print(0)