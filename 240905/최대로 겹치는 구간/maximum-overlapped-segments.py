N = int(input())

array = [0] * (200 + 1)

for _ in range(N):
    start, end = map(int, input().split())
    for i in range(start - 1 , end):
        array[i + 100] += 1

max_dupl = max(array)

# print(array)

print(array.count(max_dupl) + 1)