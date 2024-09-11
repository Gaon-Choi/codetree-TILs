N = int(input())

arr = []

arr.append(1)
arr.append(1)

for i in range(2, N-2):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N - 1])