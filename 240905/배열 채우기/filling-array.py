arr = list(map(int, input().split()))

temp = []

while (True):
    if arr[0] == 0:
        break
    else:
        temp.append(arr.pop(0))

temp.reverse()

for elem in temp:
    print(elem, end=" ")