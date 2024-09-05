n = int(input())

arr = [0] * 10

array = list(map(int, input().split()))

for elem in array:
    arr[elem] += 1

for i in range(1, 10):
    print(arr[i])