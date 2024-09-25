def is_all_more_than_t(temp_arr, t):
    for elem in temp_arr:
        if elem <= t:
            return False
    return True

n, t = map(int, input().split())

arr = list(map(int, input().split()))

temp = []

for i in range(n):
    for j in range(i+1, n):
        if is_all_more_than_t(arr[i:j+1], t):
            temp.append(j-i)

if temp:
    print(max(temp) + 1)
else:
    print(0)