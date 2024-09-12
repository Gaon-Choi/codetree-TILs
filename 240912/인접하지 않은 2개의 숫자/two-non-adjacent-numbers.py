n = int(input())

arr = list(map(int, input().split()))

result = []

for i in range(n):
    for j in range(i + 2, n):
        result.append(arr[i] + arr[j])

print(max(result))