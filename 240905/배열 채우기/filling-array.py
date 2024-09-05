arr = list(map(int, input().split()))

temp = []
original_length = arr
cnt = 1

while (True):
    if (len(arr) >= 1 and arr[0] == 0) or original_length == cnt:
        break
    else:
        temp.append(arr.pop(0))
        cnt += 1

temp.reverse()

for elem in temp:
    print(elem, end=" ")