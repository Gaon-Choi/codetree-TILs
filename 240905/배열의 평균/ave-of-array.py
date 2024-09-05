arr = []

row = 2; col = 4

for _ in range(row):
    arr.append(list(map(int, input().split())))

row_avg = []
col_avg = []
total_sum = 0

for r in arr:
    row_avg.append(sum(r) / len(r))
    total_sum += sum(r)

for i in range(col):
    tmp = 0
    for j in range(row):
        tmp += arr[j][i]
    col_avg.append(tmp / row)

for data in row_avg:
    print(format(data, ".1f"), end=" ")
print()

for data in col_avg:
    print(format(data, ".1f"), end=" ")
print()

print(format(total_sum/(row*col), ".1f"))