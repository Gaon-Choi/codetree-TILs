def calculate_distance(arr: list):
    total_dist = []
    dist = 0

    for seat in arr:
        if seat == 1:
            total_dist.append(dist)
            dist = 0
        dist += 1

    total_dist.pop(0)

    return min(total_dist)

N = int(input())

# 0 : 비어 있음, 1 : 점유중
seats = list(map(int, list(input())))

answer_list = []

for seat in range(N):

    if seats[seat] == 0:
        seats[seat] = 1

        answer_list.append(calculate_distance(seats))

        seats[seat] = 0

print(max(answer_list))