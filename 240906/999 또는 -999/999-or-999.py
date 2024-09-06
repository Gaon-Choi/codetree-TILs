temp = list(map(int, input().split()))

arr = []

for elem in temp:
    if elem == 999 or elem == -999:
        break
    arr.append(elem)

print(max(arr), min(arr))