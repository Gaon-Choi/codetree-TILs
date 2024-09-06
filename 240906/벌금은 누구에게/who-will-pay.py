N, M, K = map(int, input().split())

student = list(range(1, N+1))
punish = []

for _ in range(N):
    punish.append(int(input()))

for p in punish:
    student[p-1] -= 1
    if 0 in student:
        print(student.index(0) + 1)
        break