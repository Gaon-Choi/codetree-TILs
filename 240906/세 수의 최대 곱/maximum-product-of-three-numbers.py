n = int(input())

arr = list(map(int, input().split()))

temp = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            temp.append(arr[i] * arr[j] * arr[k])

print(max(temp))