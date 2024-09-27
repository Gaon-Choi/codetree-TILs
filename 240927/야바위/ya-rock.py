N = int(input())

games = list()

for _ in range(N):
    games.append(list(map(int, input().split())))

scores = []

for i in range(1, 3 + 1):
    arr = []

    for j in range(1, 3+1):
        arr.append(1 if j == i else 0)

    score = 0

    for game in games:
        arr[game[0] - 1], arr[game[1] - 1] = arr[game[1] - 1], arr[game[0] - 1]

        if arr[game[2] - 1] == 1:
            score += 1

    scores.append(score)

print(max(scores))