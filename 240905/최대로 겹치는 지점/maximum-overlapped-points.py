start = 1
end = 100

offset = -1

arr = [0] * (end - start + 1)

N = int(input())

for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        arr[i + offset] += 1

print(max(arr))