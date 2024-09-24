size = 1000

arr = [0] * (2 * size + 1)

n = int(input())

curr = size

for _ in range(n):
    loc, direction = input().split()
    loc = int(loc)

    if direction == "R":
        for _ in range(loc):
            arr[curr] += 1
            curr += 1
    else:
        for _ in range(loc):
            arr[curr] += 1
            curr -= 1

print(len(list(filter(lambda x: x >= 2, arr))))