N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

temp = []

for _ in range(N):
    arr = arr[1:] + [arr[0]]

    temp.append(sum(idx * value for idx, value in enumerate(arr)))

print(min(temp))