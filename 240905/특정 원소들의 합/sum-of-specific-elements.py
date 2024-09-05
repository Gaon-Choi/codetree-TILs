size = 4

arr = []

for _ in range(size):
    arr.append(list(map(int, input().split())))

total = 0
for i in range(size):
    for j in range(i + 1):
        total += arr[i][j]

print(total)