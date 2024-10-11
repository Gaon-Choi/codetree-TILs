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

for seat1 in range(N):
    for seat2 in range(seat1, N):

        if seats[seat1] == 0 and seats[seat2] == 0:
            seats[seat1] = 1
            seats[seat2] = 1

            answer_list.append(calculate_distance(seats))

            seats[seat1] = 0
            seats[seat2] = 0

print(max(answer_list))