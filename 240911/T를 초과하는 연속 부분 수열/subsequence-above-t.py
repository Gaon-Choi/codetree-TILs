n, t = map(int, input().split())

arr = list(map(int, input().split()))
temp_arr = []

counts = []

for i in range(n):
    elem = arr[i]
    if elem <= t:
        if len(temp_arr) > 0:
            counts.append(len(temp_arr))
            temp_arr = []
        continue
    if len(temp_arr) == 0 or temp_arr[-1] < elem :
        temp_arr.append(elem)
    else:
        counts.append(len(temp_arr))
        temp_arr = [elem]

if len(temp_arr) > 0:
    counts.append(len(temp_arr))

print(max(counts))