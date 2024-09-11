N = int(input())

arr = [0] * 101

for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        arr[i] += 1

if N in arr:
    print("Yes")
else:
    print('No')