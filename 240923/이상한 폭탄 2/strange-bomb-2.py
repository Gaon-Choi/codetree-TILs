N, K = map(int, input().split())

bomb_list = []

for _ in range(N):
    bomb_list.append(int(input()))

bomb_set = set(bomb_list)
bomb_answer = []

for bomb in bomb_set:
    bomb_idx_list = [index for index, value in enumerate(bomb_list) if value == bomb]
    dist_value = []

    for i in range(len(bomb_idx_list) - 1):
        dist_value.append(abs(bomb_idx_list[i] - bomb_idx_list[i + 1]))

    if dist_value and max(dist_value) <= K:
        bomb_answer.append(bomb)

if bomb_answer:
    print(max(bomb_answer))
else:
    print(-1)