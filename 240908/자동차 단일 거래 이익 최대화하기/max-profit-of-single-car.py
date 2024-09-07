N = int(input())

arr = list(map(int, input().split()))

revenue = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        revenue.append(arr[j] - arr[i])
        
print(max(revenue))