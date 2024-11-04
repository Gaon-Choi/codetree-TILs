arr = []

n = int(input())

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, +1))
    arr.append((end, -1))

arr.sort()

cnt = 0
max_cnt = 0

for point, val in arr:
    cnt += val
    max_cnt = max(cnt, max_cnt)

print(max_cnt)