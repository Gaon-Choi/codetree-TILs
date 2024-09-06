N = int(input())

house_loc = list(map(int, input().split()))

result = []

for i in range(len(house_loc)):
    tmp = 0
    curr_loc = i

    for idx, value in enumerate(house_loc):
        tmp += value * abs(curr_loc - idx)

    result.append(tmp)

print(min(result))