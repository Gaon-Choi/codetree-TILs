N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = -1
    else:
        arr[i] = 1

prev = None

tmp_list = []
result = []

print(arr)

for elem in arr:
    if (len(tmp_list) > 0) and (tmp_list[-1] * elem < 0):
        result.append(len(tmp_list))
        tmp_list.clear()
    tmp_list.append(elem)

result.append(len(tmp_list))

print(max(result))