n = int(input())

arr = list(map(int, input().split()))

count = 0
two_third_idx = -1

for idx, elem in enumerate(arr):
    if elem == 2:
        count += 1

    if count == 3:
        two_third_idx = idx
        break

print(two_third_idx + 1)