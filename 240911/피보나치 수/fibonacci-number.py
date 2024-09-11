N = int(input())

arr = [0] * 45

arr[0] = 1
arr[1] = 1

for i in range(2, 45):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N - 1])