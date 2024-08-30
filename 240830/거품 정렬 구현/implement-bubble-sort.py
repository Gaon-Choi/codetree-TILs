N = int(input())

arr = list(map(int, input().split()))

for _ in range(N):
    for i in range(N - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

for elem in arr:
    print(elem, end=" ")