N = int(input())

worker = []

for _ in range(N):
    worker.append(list(map(int, input().split())))

results = []

for i in range(N):
    work_timeline = [0] * 1000
    for j in range(N):
        if i != j:
            for k in range(worker[j][0], worker[j][1]):
                work_timeline[k] = 1
            # work_timeline[worker[j][0]:worker[j][1]] = 1

    results.append(sum(work_timeline))

print(max(results))