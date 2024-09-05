start = 1
end = 100

offset = -1

arr = [0] * (end - start)

N = int(input())

for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e):
        arr[i + offset] += 1

print(max(arr) + 1)