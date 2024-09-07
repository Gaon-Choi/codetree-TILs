n = int(input())

arr = [None for _ in range(100000)]

curr = 0

for _ in range(n):
    dist, direction = input().split()
    dist = int(dist)

    if direction == "R":
        for i in range(dist):
            arr[curr + i] = True
        curr = curr + (dist - 1)

    else:
        for i in range(dist):
            arr[curr - i] = False
        curr = curr - (dist - 1)

print(arr.count(False), arr.count(True))