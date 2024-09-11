N = int(input())

arr = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        total_sum = sum(arr[i:j]) // len(arr[i:j])
        if total_sum in arr[i:j]:
            cnt += 1

print(cnt)