N, M, K = map(int, input().split())

student = [0] * N
punish = []

for _ in range(M):
    punish.append(int(input()))

for p in punish:
    student[p-1] += 1
    if K in student:
        print(student.index(K) + 1)
        break

print(-1)