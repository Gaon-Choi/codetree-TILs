N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

average = sum(arr) // N

result = 0

for elem in arr:
    if elem < average:
        result += (average - elem)

print(result)