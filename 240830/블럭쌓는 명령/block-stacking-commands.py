n, k = map(int, input().split())

container = [0] * n

for _ in range(k):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        container[i] += 1

container.sort()

print(container[len(container) // 2])