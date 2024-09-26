N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

height = 0

answers = []

while height <= max(arr):
    count = 0

    prev_is_upper = False

    for elem in arr:
        if elem - height > 0:
            if not prev_is_upper:
                prev_is_upper = True
        else:
            if prev_is_upper:
                count += 1
            prev_is_upper = False

    if prev_is_upper:
        count += 1

    answers.append(count)

    height += 1

print(max(answers))