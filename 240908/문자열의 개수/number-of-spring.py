arr = []

while(True):
    val = input()

    if val == "0":
        break

    else:
        arr.append(val)

print(len(arr))

for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])