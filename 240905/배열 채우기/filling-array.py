arr = list(map(int, input().split()))

temp = []

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        temp.append(arr[i])

temp.reverse()

for elem in temp:
    print(elem, end=" ")