N = int(input())

arr = list(map(int, input().split()))

locations = []

while(len(arr) >= 1):
    maxima_idx = arr.index(max(arr))
    locations.append(maxima_idx + 1)
    arr = arr[0:maxima_idx]

for elem in locations:
    print(elem, end=" ")