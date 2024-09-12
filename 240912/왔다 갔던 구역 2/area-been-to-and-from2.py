location = dict()

N = int(input())

curr_x = 0

for _ in range(N):
    dist, direction = input().split()
    dist = int(dist)

    if direction == "L":
        for __ in range(dist):
            curr_x -= 1
            if curr_x in location:
                location[curr_x] += 1
            else:
                location[curr_x] = 1
    else:
        for __ in range(dist):
            curr_x += 1
            if curr_x in location:
                location[curr_x] += 1
            else:
                location[curr_x] = 1
                
dist_values = location.values()
result = 0

for elem in dist_values:
    if elem >= 2:
        result += 1

print(result)