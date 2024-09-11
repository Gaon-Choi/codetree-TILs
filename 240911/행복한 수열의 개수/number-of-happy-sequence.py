def is_ideal_series(num_list, m):
    temp_arr = []
    counts = []

    for elem in num_list:
        if len(temp_arr) == 0 or temp_arr[-1] == elem:
            temp_arr.append(elem)
        else:
            counts.append(len(temp_arr))
            temp_arr = [elem]

    if len(temp_arr) > 0:
        counts.append(len(temp_arr))

    if len(list(filter(lambda x: x >= m, counts))) >= 1:
        return True
    return False

happy_count = 0

matrix = []

n, m = map(int, input().split())
for _ in range(n):
    sub_row = map(int, input().split())
    matrix.append(list(sub_row))

for row in matrix:
    if is_ideal_series(row, m):
        happy_count += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])

    if is_ideal_series(temp, m):
        happy_count += 1

print(happy_count)