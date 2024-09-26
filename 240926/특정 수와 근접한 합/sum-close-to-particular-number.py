N, S = map(int, input().split())

arr = list(map(int, input().split()))

answers = []

for i in range(N):
    for j in range(i + 1, N):
        answers.append(abs(S - sum(value for idx, value in enumerate(arr) if idx != i and idx != j)))

print(min(answers))