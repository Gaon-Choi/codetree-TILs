arr = list(map(int, input().split()))

temp = []

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        temp.append(arr[i])

print(sum(temp), format(sum(temp) / len(temp), ".1f"))