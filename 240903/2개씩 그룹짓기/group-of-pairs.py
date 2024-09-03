N = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = []

for i in range(2 * N):
    result.append(arr[i] + arr[2*N - 1 - i])

print(max(result))